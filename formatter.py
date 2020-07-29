
def validDate(date):
    if date is not None and date.isNumeric:
        try:
            dateutil.parser.parse(date)
            return True
        except ValueError:
            return False
    else:
        return False

DateFormat = '%d-%m-%Y'
df["dob"] = df["dob"].apply(lambda x: dateutil.parser.parse(x).strftime(DateFormat) if validDate(x) else 'NaN')