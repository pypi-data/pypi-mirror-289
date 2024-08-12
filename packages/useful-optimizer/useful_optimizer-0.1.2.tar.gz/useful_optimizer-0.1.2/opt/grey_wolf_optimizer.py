"""Grey Wolf Optimizer (GWO) Algorithm.

!!! warning

    This module is still under development and is not yet ready for use.

This module implements the Grey Wolf Optimizer (GWO) algorithm. GWO is a metaheuristic
optimization algorithm inspired by grey wolves. The algorithm mimics the leadership
hierarchy and hunting mechanism of grey wolves in nature. Four types of grey wolves
such as alpha, beta, delta, and omega are employed for simulating the hunting behavior.

The GWO algorithm is used to solve optimization problems by iteratively trying to
improve a candidate solution with regard to a given measure of quality, or fitness
function.

Example:
    optimizer = GreyWolfOptimizer(func=objective_function, lower_bound=-10,
    upper_bound=10, dim=2, pack_size=20, max_iter=1000)
    best_solution, best_fitness = optimizer.search()
    print(f"Best solution found: {best_solution}")
    print(f"Best fitness found: {best_fitness}")

Attributes:
    func (Callable): The objective function to optimize.
    lower_bound (float): The lower bound of the search space.
    upper_bound (float): The upper bound of the search space.
    dim (int): The dimension of the search space.
    pack_size (int): The size of the wolf pack (candidate solutions).
    max_iter (int): The maximum number of iterations.

Methods:
    search(): Perform the GWO optimization.
"""

from __future__ import annotations

import numpy as np

from opt.abstract_optimizer import AbstractOptimizer
from opt.benchmark.functions import shifted_ackley


class GreyWolfOptimizer(AbstractOptimizer):
    """Implementation of the Grey Wolf Optimizer algorithm.

    This optimizer is inspired by the hunting behavior of grey wolves in nature.
    It iteratively updates the positions of a population of wolves to search for
    the optimal solution to a given optimization problem.

    Attributes:
        seed (int): The seed value for the random number generator.
        lower_bound (float): The lower bound of the search space.
        upper_bound (float): The upper bound of the search space.
        population_size (int): The number of wolves in the population.
        dim (int): The dimensionality of the problem.
        max_iter (int): The maximum number of iterations.
        func (callable): The objective function to be minimized.

    """

    def search(self) -> tuple[np.ndarray, float]:
        """Run the Grey Wolf Optimizer algorithm.

        Returns:
            Tuple[np.ndarray, float]: A tuple containing the best solution found
            and its corresponding fitness value.

        """
        # Initialize population and fitness
        population = np.random.default_rng(self.seed).uniform(
            self.lower_bound, self.upper_bound, (self.population_size, self.dim)
        )
        fitness = np.apply_along_axis(self.func, 1, population)

        # Initialize alpha, beta, and delta wolves
        alpha = beta = delta = population[np.argmin(fitness)]

        # Main loop
        for iter_count in range(self.max_iter):
            self.seed += 1
            a = 2 - iter_count * ((2) / self.max_iter)  # Linearly decreasing a

            for i in range(self.population_size):
                self.seed += 1
                # Compute distances to alpha, beta, and delta
                dist_alpha = abs(alpha - population[i])
                dist_beta = abs(beta - population[i])
                dist_delta = abs(delta - population[i])

                # Compute hunting (searching) behavior
                x1 = alpha - a * dist_alpha
                x2 = beta - a * dist_beta
                x3 = delta - a * dist_delta

                # Update position
                population[i] = (x1 + x2 + x3) / 3 + np.random.default_rng(
                    self.seed
                ).random() * (x1 + x2 + x3) / 3

                # Ensure the position stays within the bounds
                population[i] = np.clip(
                    population[i], self.lower_bound, self.upper_bound
                )

                # Update fitness
                fitness[i] = self.func(population[i])

            # Update alpha, beta, and delta wolves
            sorted_indices = np.argsort(fitness)
            alpha = population[sorted_indices[0]]
            beta = population[sorted_indices[1]]
            delta = population[sorted_indices[2]]

        # Get best solution
        best_solution = alpha
        best_fitness = self.func(best_solution)

        return best_solution, best_fitness


if __name__ == "__main__":
    optimizer = GreyWolfOptimizer(
        shifted_ackley, dim=2, lower_bound=-2.768, upper_bound=+2.768
    )
    best_solution, best_fitness = optimizer.search()
    print(f"Best solution found: {best_solution}")
    print(f"Best fitness found: {best_fitness}")
