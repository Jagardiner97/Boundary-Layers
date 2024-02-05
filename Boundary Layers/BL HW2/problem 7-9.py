import pandas as pd
import matplotlib.pyplot as plt

# Constants and Properties
D_h = 0.1
rho = 1000
Pr = 6.9
mu = 0.89e-3
cp = 4182
Re = 1000
L = 10
V = 8.9e-3

# Equations
def cfm(x_vals, tau_vals, rho, u_mean, D, Reynolds):
    denominator = 0.5 * rho * (u_mean ** 2)
    cfm_vals = []
    for index, x in enumerate(x_vals):
        x_prev = 0
        integral = 0
        for i in range(index):
            x_curr = x_vals[i] * D
            dx = x_curr - x_prev
            integral += tau_vals[i] * dx
            x_prev = x_curr
        integral /= (x * D)
        cfm_vals.append(integral * Reynolds / denominator)
    return cfm_vals

def cf_app(x_vals, dp_vals, Reynolds, rho, u_mean):
    cf_app = []
    for index, x in enumerate(x_vals):
        cf = dp_vals[index] * Reynolds / (2 * x * rho * (u_mean ** 2))
        cf_app.append(cf)
    return cf_app

# plot local, mean, and apparent friction coefficient vs x+
# Read the data using pandas
file_path = 'ftn85.txt'
data = pd.read_csv(file_path, delim_whitespace=True, skiprows=1)  # Assuming the data starts from the 3rd row

# Extract the data
x_D = data.iloc[:, 0].values
tau_w = data.iloc[:, 2].values
cf2 = data.iloc[:, 4].values
delp = data.iloc[:, 5].values

# Calculate values
cf_loc_vals = cf2 * 2 * Re
cf_mean_vals = cfm(x_D, tau_w, rho, V, D_h, Re)
cf_app_vals = cf_app(x_D, delp, Re, rho, V)
Rexd = Re / x_D

# Plot the data using matplotlib
plt.plot(Rexd, cf_loc_vals, label='cf local')
plt.plot(Rexd, cf_mean_vals, label='cf mean')
plt.plot(Rexd, cf_app_vals, label='cf apparent')

# Customize the plot
plt.xlabel('Re/x/D_h')
plt.ylabel('cf * Re')
plt.title('Friction Coefficients')
plt.legend()
plt.xlim(6, 500)
plt.ylim(10, 80)
plt.show()


# confirm hydrodynamic entry length and compare
L_fd = D_h * Re / 20

file_path_out = "out.txt"
data_out = pd.read_csv(file_path_out, delim_whitespace=True, skiprows=19)

x_dh_re = data_out.iloc[:, 1].values
u_cl = data_out.iloc[:, 3].values
plt.plot(x_dh_re, u_cl, label="Centerline Velocity")
plt.axvline(x=0.05, color='red', linestyle='--', label="Predicted x_fd")
plt.xlabel("x/D_h/Re")
plt.ylabel("Centerline Velocity (m/s)")
plt.title("Determining Hydrodynamic Entry Length")
plt.legend()
plt.show()

# plot nondimensional velocity profiles at various x+ locations
rows_per_profile = 64
cols_to_use = [1, 2, 3, 4, 5]
file_path_profiles = "fig 7-6 data.txt"
profile0 = pd.read_csv(file_path_profiles, delim_whitespace=True, skiprows=24, nrows=rows_per_profile, usecols=cols_to_use)
profile70 = pd.read_csv(file_path_profiles, delim_whitespace=True, skiprows=93, nrows=rows_per_profile, usecols=cols_to_use)
profile202 = pd.read_csv(file_path_profiles, delim_whitespace=True, skiprows=162, nrows=rows_per_profile, usecols=cols_to_use)
profile333 = pd.read_csv(file_path_profiles, delim_whitespace=True, skiprows=231, nrows=rows_per_profile, usecols=cols_to_use)
profile463 = pd.read_csv(file_path_profiles, delim_whitespace=True, skiprows=300, nrows=rows_per_profile, usecols=cols_to_use)

r0 = profile0.iloc[:, 2].values
uv0 = profile0.iloc[:, 3].values
label0 = f"(x/D)/Re = {0/Re}"

r70 = profile70.iloc[:, 2].values
uv70 = profile70.iloc[:, 3].values
label70 = f"(x/D) = {3.5e-1 / Re}"

r202 = profile202.iloc[:, 2].values
uv202 = profile202.iloc[:, 3].values
label202 = f"(x/D) = {3.5 / Re}"

r333 = profile333.iloc[:, 2].values
uv333 = profile333.iloc[:, 3].values
label333 = f"(x/D) = {3.5e1 / Re}"

r463 = profile463.iloc[:, 2].values
uv463 = profile463.iloc[:, 3].values
label463 = f"(x/D) = {1e2 / Re}"

plt.plot(r0, uv0, label=label0)
plt.plot(r70, uv70, label=label70)
plt.plot(r202, uv202, label=label202)
plt.plot(r333, uv333, label=label333)
plt.plot(r463, uv463, label=label463)

plt.title("Nondimensional Velocity Profiles")
plt.xlabel("r/r_s")
plt.ylabel("u/V")
plt.legend()
plt.xlim(0, 1)
plt.ylim(0, 3)
plt.show()

# plot the absolute value of the pressure gradient vs x+
plt.plot(x_D / Re, delp)
plt.xlabel("x+")
plt.ylabel("dP/dx")
plt.title("Pressure Gradient vs x+")
plt.show()

# plot the ratio of centerline velocity to mean velocity and plot it vs x+ (show becomes 2)
plt.plot(x_D / Re, u_cl)
plt.xlabel("x+")
plt.ylabel("u_cl/V")
plt.title("Centerline Velocity to Mean Velocity Ratio")
plt.show()
