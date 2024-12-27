import pydykit
import pydykit.postprocessors as postprocessors
import pydykit.systems_port_hamiltonian as phs

name = "four_particle_system"

manager = pydykit.managers.Manager()

path_config_file = f"./input_files/{name}.yml"

manager.configure_from_path(path=path_config_file)

porthamiltonian_system = phs.PortHamiltonianMBS(manager=manager)
# creates an instance of PHS with attribute MBS
manager.system = porthamiltonian_system

result = pydykit.results.Result(manager=manager)
result = manager.manage(result=result)

df = result.to_df()
postprocessor = postprocessors.Postprocessor(
    manager,
    state_results_df=df,
)
plotter = postprocessors.Plotter(results_df=postprocessor.results_df)

postprocessor.postprocess(
    quantities_and_evaluation_points={
        "hamiltonian": [
            "current_time",
            "interval_increment",
        ],
        "constraint": ["current_time"],
        "constraint_velocity": ["current_time"],
    }
)

postprocessor.postprocess(
    quantities_and_evaluation_points={"dissipated_work": ["interval_midpoint"]}
)

postprocessor.add_sum_of(
    quantities=["hamiltonian_interval_increment", "dissipated_work_interval_midpoint"],
    sum_name="sum",
)

fig01 = plotter.visualize_time_evolution(quantities=["hamiltonian_current_time"])
fig01.show()

postprocessor.results_df["abs_sum"] = abs(postprocessor.results_df["sum"])

fig02 = plotter.visualize_time_evolution(
    quantities=[
        "hamiltonian_interval_increment",
        "dissipated_work_interval_midpoint",
        "abs_sum",
    ],
)
fig02.show()

fig03 = plotter.visualize_time_evolution(
    quantities=["abs_sum"], y_axis_scale="log", y_axis_label="abs_sum"
)
fig03.show()

fig04 = plotter.visualize_time_evolution(
    quantities=["constraint_current_time"], y_axis_label="constraints"
)
fig04.show()

fig05 = plotter.visualize_time_evolution(
    quantities=["constraint_velocity_current_time"], y_axis_label="velocity constraints"
)
fig05.show()

# postprocessor.results_df.to_csv(f"./results/{name}.csv", index=False)
