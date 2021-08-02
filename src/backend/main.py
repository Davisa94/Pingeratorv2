import dbConnect as dbConnect
import  dbInteract as DBI


def main():
    try:
        myDB = dbConnect()
        db_connection = myDB.connect()
        db_interactor = DBI(db_connection)

        db_interactor.insertSpeed()
    # Close the connection
    except Exception as e:
        print("An unexpected exeception has occured:{}".format(e))
    finally:
        db_connection.close()




if __name__ == '__main__':
    main()