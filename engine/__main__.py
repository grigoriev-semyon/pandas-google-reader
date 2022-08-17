from engine.methods.reader import get_data_google_sheets


if __name__ == "__main__":
    df_ = get_data_google_sheets("1m5bZVSYC6jklG59VLhI8fRF4OTshBZSrWm5v7IMhB_M")
    for row in df_:
        row.head()
    print(df_)
