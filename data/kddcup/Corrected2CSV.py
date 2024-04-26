import pandas as pd

# File path
KDD_fp = 'data\kddcup\kddcup.data.corrected'

# List of attribute names
attribute_names = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
    "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted", "num_root", "num_file_creations",
    "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login", "is_guest_login",
    "count", "srv_count", "serror_rate", "srv_serror_rate", "rerror_rate", "srv_rerror_rate",
    "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
    "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",
    "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "type",
]

# Read the data into a DataFrame without specifying column headers
CORRECTED = pd.read_csv(KDD_fp, header= None, names= attribute_names)

# Set the first column as the index of the DataFrame
CORRECTED.set_index('duration', inplace=True)

# Now, remove the 'duration' column, which is the actual index now
CORRECTED.reset_index(drop=True, inplace=True)

# Convert the DataFrame to a CSV file
CORRECTED.to_csv('kddcup_corrected.csv', index= False)