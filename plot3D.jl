using CSV
using DataFrames
using Plots
using PlotlyJS



#=  Set the backend to PlotlyJS for interactive plots
 =#
Plots.plotlyjs()

# Load the data from the CSV file
df_1 = CSV.read("data/1x50bin_0.021m 1.csv", DataFrame)

# Rename columns
column_names = ["time"; ["h2o_mf_bin$i" for i in 1:(size(df_1, 2)-2)]...; "Temp"]
rename!(df_1, Symbol.(column_names))

# Extract data for plotting
time = df_1.time
positions = 1:(size(df_1, 2)-2)
h2o_mf = [df_1[!, Symbol("h2o_mf_bin$i")] for i in positions]

# Create 3D plot
plot3d = Plots.plot()
for (i, h2o_mf_bin) in enumerate(h2o_mf)
  Plots.plot!(plot3d, time, fill(i, length(time)), h2o_mf_bin, label="Bin $i")
end

xlabel!("Time")
ylabel!("Position")
zlabel!("H2O Mass Fraction")

title!("H2O Mass Fraction(x, time)")


display(plot3d)