import csv
import pandas as pd

# Read CSV file and created a dataframe
df = pd.read_csv(r'Excel-erate Application.csv')

# TODO: Make this program runnable without an ide

def trim_dictionary(input_dict, target_size):
    while len(input_dict) > target_size:
        input_dict.popitem()
    return input_dict

def applicantaccepter(target_size):

    # Create priority lists and accepted applicants
    acceptedPatrons = {}
    income= {}
    education = {}
    identity = {}

    for i in range(len(df)):
        # Accepts all
        if len(df) <= target_size:
            acceptedPatrons.update({df.iloc[i, 2]: df.iloc[i, 1]})
            return acceptedPatrons

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

    acceptedPatrons = income | education | identity

    if len(acceptedPatrons) < target_size:
        for i in range(len(df)):
            while len(df) <= target_size:
                if df.iloc[i, 2] not in acceptedPatrons:
                    acceptedPatrons.update({df.iloc[i, 2]: df.iloc[i, 1]})

    return acceptedPatrons

def main():
    # TODO: have the input checked for any letters or symbols, and removed
    target_size = int(input("Enter the maximum size of the class: ").strip())
    if target_size < 1 or target_size > len(df):
        while target_size < 1 or target_size > len(df):
            target_size = int(input("Please enter a valid size: "))

    acceptedPatrons = applicantaccepter(target_size)
    print(len(acceptedPatrons))
    # with open('acceptedPatrons.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(['Name', 'Email'])
    #     for name, email in acceptedPatrons.items():
    #         writer.writerow([name, email])

    # acceptedPatrons, waitlistedPatrons = applicantaccepter(target_size)
    # with open('acceptedPatrons.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(['Name', 'Email', 'Waitlisted Name', 'Waitlisted Email'])
    #     for name, email in acceptedPatrons.items():
    #         for waitlistedName, waitlistedEmail in waitlistedPatrons.items():
    #             writer.writerow([name, email, waitlistedName, waitlistedEmail])


if __name__ == '__main__':
    main()