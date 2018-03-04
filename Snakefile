rule create_data:
    output:
        "some-data.csv"
    run:
        import pandas as pd
        data = pd.Series([1, 2, 3, 4, 5])
        data.to_csv(output[0])

onsuccess:
    shell("py.test")
