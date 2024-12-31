import csv
import pandas as pd

# Read CSV file and created a dataframe
df = pd.read_csv(r'Excel-erate Application.csv')

# TODO: Make this program runnable without an ide

def trim_dictionary(input_dict, target_size):
    while len(input_dict) > target_size:
        input_dict.popitem()
    return input_dict

def waitlistApplicants(acceptedPatrons, target_size):
    waitlistedPatrons = {}
    for i in range(len(df)):
        name = df.iloc[i, 2]
        email = df.iloc[i, 1]
        if len(waitlistedPatrons) < target_size and name not in acceptedPatrons and email not in acceptedPatrons:
            waitlistedPatrons.update({name: email})
    
    return waitlistedPatrons

def applicantaccepter(target_size):

    # Create priority lists and accepted applicants
    acceptedPatrons = {}
    income= {}
    education = {}
    identity = {}

    for i in range(len(df)):
        # Accepts all if dataframe is same size or less than the target size
        if len(df) <= target_size:
            acceptedPatrons.update({df.iloc[i, 2]: df.iloc[i, 1]})
            return acceptedPatrons

        # Creates Priority Dictionaries
        elif ((df.iloc[i, 3] == 'Yes' and df.iloc[i, 5] == 'Yes' and df.iloc[i, 2] not in acceptedPatrons
                and not pd.isnull(df.iloc[i, 1])) and df.iloc[i, 6]
              in ['Computer, Internet', 'Computer, Internet, Microsoft Excel 2016 or above',
                  'Computer, Internet,Microsoft Excel 2016 or above, A second monitor or the ability to split-screen or toggle between multiple programs (Zoom and Excel)']):
            if df.iloc[i, 13] == 'Less than $20,000':
                income.update({df.iloc[i, 2] : df.iloc[i, 1]})

            elif (df.iloc[i, 11] == 'No High School' or df.iloc[i, 11] == 'Some High School' or
                  df.iloc[i, 11] == 'High School/GED' or df.iloc[i, 11] == 'Some College but no degree'):
                education.update({df.iloc[i, 2]: df.iloc[i, 1]})

            elif (df.iloc[i, 10] == 'Female' or df.iloc[i, 10] == 'Non-binary/third gender' or
                    df.iloc[i, 10] == 'Cisgender' or df.iloc[i, 10] == 'Agender' or df.iloc[i, 10] == 'Genderqueer' or
                    df.iloc[i, 9] == 'Asian' or df.iloc[i, 9] == 'Black, non-Hispanic' or df.iloc[i, 9] == 'Hispanic/Latino'
                    or df.iloc[i, 9] == 'Native Hawaiian/Pacific Islander' or df.iloc[i, 9] == 'Native American'):
                identity.update({df.iloc[i, 2] : df.iloc[i, 1]})
    
    # Merges Dictionaries into one
    acceptedPatrons = income | education | identity
    
    # Checks for total accepted applicants and will trim if too large or add if too small
    if len(acceptedPatrons) < target_size:
        for i in range(len(df)):
            name = df.iloc[i, 2]
            email = df.iloc[i, 1]
            if len(acceptedPatrons) < target_size and name not in acceptedPatrons and email not in acceptedPatrons:
                acceptedPatrons.update({name: email})
    elif len(acceptedPatrons) > target_size:
        acceptedPatrons = trim_dictionary(acceptedPatrons, target_size)
    
    if len(acceptedPatrons) < len(df):
        waitlistedPatrons = waitlistApplicants(acceptedPatrons, target_size)
    else:
        waitlistedPatrons = {}

    return acceptedPatrons, waitlistedPatrons

def main():
    # TODO: have the input checked for any letters or symbols, and removed
    target_size = int(input("Enter the maximum size of the class: ").strip())
    if target_size < 1 or target_size > len(df):
        while target_size < 1 or target_size > len(df):
            target_size = int(input("Please enter a valid size: "))

    acceptedPatrons, waitlistedPatrons = applicantaccepter(target_size)
    with open('acceptedPatrons.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Email', 'Waitlisted Name', 'Waitlisted Email'])
        for (accepted_name, accepted_email), (waitlisted_name, waitlist_email) in zip(acceptedPatrons.items(),
                                                                                      waitlistedPatrons.items()):
            writer.writerow([accepted_name, accepted_email, waitlisted_name, waitlist_email])

if __name__ == '__main__':
    main()