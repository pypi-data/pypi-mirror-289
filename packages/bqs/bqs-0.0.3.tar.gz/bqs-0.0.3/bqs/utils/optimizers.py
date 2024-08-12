import copy
import numpy as np
# from numpy_ml.neural_nets.optimizers import Adam as adamopt
import random as rnd
from typing import List, Callable, Tuple, Optional, Dict
from scipy.optimize import OptimizeResult, minimize
from abc import ABC, abstractmethod


from .qaoa_utils import *
from .vqa_utils import CostFunction, VariationalCircuit

# TODO: impleemntation of ADAM
class Adam:
    def __init__(
            self,
            len_param,
            initial_point=None,
            learning_rate=0.1,
            beta_1=0.9,
            beta_2=0.999,
            epsilon=1e-4,
    ):
        raise NotImplementedError("Adam optimizer not implemented yet!")
        self.p = len_param
        if type(initial_point) != np.ndarray:
            self.theta = [0. for _ in range(2*len_param)]
        else:
            self.theta = initial_point
        self.beta = self.theta[:self.p]
        self.gamma = self.theta[self.p:]
        self.learning_rate = learning_rate
        self.beta_1 = beta_1
        self.beta_2 = beta_2
        self.eps = epsilon
        self.adamopt = adamopt(lr=learning_rate, decay1=beta_1, decay2=beta_2,eps=epsilon)

    def run(self, objective_function, method, number_of_iterations=100, display=True):
        res_sample = minimize(objective_function, self.theta, method=method, options={'num_iterations': number_of_iterations, 'disp': display})
        self.theta = res_sample['x']
        return self.theta

    def optimize(self, objective_function, number_of_iterations=100, display=True, **kwargs):
        obj_params = kwargs.pop('objective_params', {})

        def _calc_grad(fun, x0, args, **kwargs)->OptimizeResult:
            if type(x0) == list:
                _theta = np.array(x0)

            grad = np.array([0. for _ in x0])

            for i in range(len(x0)):
                shift = np.pi / 2

                x0[i] += shift
                obj_params['theta'] = x0
                grad[i] = 0.5 * (fun(**obj_params))

                x0[i] -= 2*shift
                obj_params['theta'] = x0
                grad[i] -= 0.5 * (fun(**obj_params))
                x0[i] += shift

            self.adamopt.update(x0, grad, 'theta')
            # TODO: Correctly wrap numpy_ml's Adam optimizer to return an OptimizeResult object
            return OptimizeResult()

        return self.run(objective_function, method=_calc_grad, number_of_iterations=number_of_iterations, display=display)


########################################################################################################################
# Optimizer
########################################################################################################################

class Optimizer(ABC):
    def __init__(
            self,
            cost_function: CostFunction,
            circuit: VariationalCircuit
    ):

        # Get the length of hyperparameters
        self.len_param = len(circuit.hyperparameters)

        # Storing the cost function to optimize
        self.cost_function = cost_function

        # Storing the circuit to optimize
        self.circuit = circuit

        # Store the hyperparameters
        if type(circuit.hyperparameters) != np.ndarray:
            self.hyperparameters = [0. for _ in range(self.len_param)]
        else:
            self.hyperparameters = circuit.hyperparameters


    @abstractmethod
    def _run(self, _obj_fun, num_iterations, **opt_arguments) -> OptimizeResult:
        pass


    def optimize(
        self, 
        num_samples_training: int, 
        num_iterations: int, 
        **kwargs
    ) -> OptimizeResult:
        """
        Optimizes the hyperparameters.

            args: 
                num_samples_training: number of samples used to evaluate the stored cost function,
                num_iterations: number of random generated sets of hyperparameters,

                circuit_options: dictionary with options for the method VariationalCircuit().sample
                opt_arguments: dictionary containing keywords and argument to give to the optimizer.
                kwargs: optional arguments for the sample evaluation.

            returns: the best hyperparameters found.
        """

        circuit_options = kwargs.pop('circuit_options', {})
        opt_arguments = kwargs.pop('opt_arguments', {})

        def _obj_fun(_theta):

            circuit_options['hyperparameters'] = _theta

            solutions = self.circuit.sample(num_samples=num_samples_training, **circuit_options)

            # Storing the mean_energy and deleting the solutions used to save RAM
            mean_energy = np.float32(self.cost_function.evaluate_samples(solutions, **kwargs))
            del solutions

            return mean_energy

        response =  self._run(_obj_fun, num_iterations=num_iterations, **opt_arguments)

        self.hyperparameters = response['x']
        self.circuit.hyperparameters = self.hyperparameters

        return response

        
class MonteCarlo(Optimizer):
    """
    Random guesser that inspects the search space by generating a random set of hyperparameters. It keeps the best set of hyperparameters generated.
    """
    def __init__(self, cost_function: CostFunction, circuit: VariationalCircuit):
        super().__init__(cost_function, circuit)


    def _run(self, _obj_fun, num_iterations, **opt_arguments):

        # Collects the optional argument passed to the optimzer
        bounds = opt_arguments.pop('bounds', [(0., 2*np.pi) for _ in range(self.len_param)])
        all_iter = opt_arguments.pop('all_iter', False)
        if all_iter:
            all_iter_list = list()

        # Setting the initial values
        current_params = self.hyperparameters
        best_params = current_params
        best_feval = _obj_fun(best_params)
        n_fevals = 1
        iteration_counter = 0

        while iteration_counter < num_iterations:
            
            # Evaluating the hyperparameters
            current_eval = _obj_fun(current_params)

            if current_eval < best_feval:
                best_feval = current_eval
                best_params = current_params

            # In case, collecting the output point of this iteration
            if all_iter:
                all_iter_list.append(best_feval)

            # Preparation fro next iteration
            iteration_counter += 1
            n_fevals += 1
            current_params = np.array([rnd.uniform(*bound) for bound in bounds])


        # Manage the output according to the input
        output_dict = {
            'fun' : best_feval,
            'x' : best_params,
            'nit' : iteration_counter,
            'nfev' : n_fevals
        }

        if all_iter:
            output_dict.update({
                'all_iter' : np.array(all_iter_list)
            })

        return OptimizeResult(**output_dict)


class COBYLA(Optimizer):
    """
    Constrained Optimization by Linear Approximation optimizer.
    """
    def __init__(self, cost_function: CostFunction, circuit: VariationalCircuit):
        super().__init__(cost_function, circuit)
    

    def _run(self, objective_function, num_iterations: int, display: bool=False, **kwargs):
        """
        Optimizes the hyperparameters of the give VQA by using COBYLA.

            args:
                num_iterations: upper limit on the number of iterations before the convergence.,
                display: displays information about the optimization subroutine if true.

                kwargs: optional arguments for the optimizer.
            
            returns: Best hyperparameters found
        """
        res_sample = minimize(
            objective_function, 
            self.hyperparameters, 
            method='COBYLA', 
            options={'num_iterations': num_iterations, 'disp': display},
            **kwargs
        )

        return res_sample


    def optimize(
        self, 
        num_samples_training: int, 
        num_iterations: int, 
        display=False, 
        **kwargs
    ):
        """
        Optimizes the hyperparameters.

            args: 
                num_samples_training: number of samples used to evaluate the stored cost function,
                num_iterations: number of random generated sets of hyperparameters,
                display: display the best expectation values and hyperparameters if true,

                circuit_options: dictionary with options for the method VariationalCircuit().sample
                opt_arguments: dictionary containing keywords and argument to give to the optimizer.
                kwargs: optional arguments for the sample evaluation.

            returns: the best hyperparameters found.
        """

        circuit_options = kwargs.pop('circuit_options', {})
        opt_arguments = kwargs.pop('opt_arguments', {})

        def _obj_fun(_theta):

            circuit_options['hyperparameters'] = _theta

            solutions = self.circuit.sample(num_samples=num_samples_training, **circuit_options)

            # Storing the mean_energy and deleting the solutions used to save RAM
            mean_energy = np.float32(self.cost_function.evaluate_samples(solutions, **kwargs))
            del solutions

            return mean_energy

        response =  self._run(_obj_fun, num_iterations=num_iterations, display=display, **opt_arguments)
        
        # For a nicer visualization
        if display:
            print()

        self.hyperparameters = response['x']
        self.circuit.hyperparameters = self.hyperparameters

        return self.hyperparameters


class SPSA(Optimizer):
    """
    Simultaneous perturbation stochastic approximation optimizer.
    """
    def __init__(self, cost_function: CostFunction, circuit: VariationalCircuit):
        super().__init__(cost_function, circuit)


    def _run(
            self,
            fun: Callable,
            num_iterations: int,
            args: Tuple = (),
            bounds: np.array = None,
            maxfev: int = np.inf,
            a: float = 1.0,
            alpha: float = 0.602,
            c: float = 1.0,
            gamma: float = 0.101,
            callback: Optional[Callable] = None,
            iteration_counter: Optional[int] = None,
            **opt_arguments: Dict

    )->OptimizeResult:
        
        # Collecting optional arguments
        all_iter = opt_arguments.pop('all_iter', False)
        if all_iter:
            all_iter_list = list()

        current_params = np.asarray(self.hyperparameters)
        n_params = self.len_param
        A = 100  # 0.01 * num_iterations

        best_params = current_params
        best_feval = fun(best_params)
        if bounds is not None:
            bounds = np.asarray(bounds)
            if np.shape(bounds) != (n_params, 2):
                raise ValueError(
                    'Pass a min and max bound for each parameter. \n {} \n {}'.format(bounds, n_params))

            def project(x):
                return np.clip(
                    x, bounds[:, 0], bounds[:, 1])

        if iteration_counter is not None:
            iteration_counter = iteration_counter
            n_fevals = 2 * iteration_counter
        else:
            iteration_counter = 0
            n_fevals = 0

        while (iteration_counter < num_iterations and n_fevals < maxfev):

            ak = a / (iteration_counter + 1.0 + A) ** alpha
            ck = c / (iteration_counter + 1.0) ** gamma
            Deltak = np.random.choice([-1, 1], size=n_params)

            iteration_counter += 1
            # Each iteration takes 2 function evaluations
            # for gradient evaluation.
            n_fevals += 2
            if bounds is not None:
                # ensure evaluation points are feasible
                # print(current_params + ck * Deltak)
                xplus = project(current_params + ck * Deltak)
                xminus = project(current_params - ck * Deltak)
                grad = (fun(xplus, *args) - fun(xminus, *args)) / (xplus - xminus)
                current_params = project(current_params - ak * grad)
            else:
                grad = ((fun(current_params + ck * Deltak, *args) -
                         fun(current_params - ck * Deltak, *args)) /
                        (2 * ck * Deltak))
                current_params = current_params - (grad * ak)

            current_feval = fun(current_params, *args)

            if current_feval < best_feval:
                best_feval = current_feval
                best_params = np.array(current_params)
                FE_best = n_fevals

            if all_iter:
                all_iter_list.append(best_feval)

            if callback:
                # Takes best parameters, best function evaluation
                # gradient and current iteration number.
                callback(best_params, best_feval,
                         current_feval, grad, iteration_counter)
                
        # Manage the output according to the input
        output_dict = {
            'fun' : best_feval,
            'x' : best_params,
            'nit' : iteration_counter,
            'nfev' : n_fevals
        }

        if all_iter:
            output_dict.update({
                'all_iter' : np.array(all_iter_list)
            })


        return OptimizeResult(**output_dict)
