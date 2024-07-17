# Salary_aggregation_tg_bot

Telegram bot with functionality for aggregating statistical data on salaries of company employees by time intervals.

<details><summary><b>Show input and output data</b></summary>

1. Example input:

    ```sh
    {
    "dt_from":"2022-09-01T00:00:00",
    "dt_upto":"2022-12-31T23:59:00",
    "group_type":"month"
    }
    ```

2. Sample output:

    ```sh
    {"dataset": [5906586, 5515874, 5889803, 6092634], "labels": ["2022-09-01T00:00:00", "2022-10-01T00:00:00", "2022-11-01T00 :00:00", "2022-12-01T00:00:00"]}
    ```

Comment to the output: the zero element of the dataset contains the sum of all payments for September, the first element contains the sum of all payments for October, etc. In the labels, the signatures correspond to the elements of the dataset.

</details>

### Cloning the repository

Clone the repository using the command below :
```bash
git clone https://github.com/BosovPN/salary_aggregation_tg_bot.git
```

### Running app in docker container

Move into directory where we have the project files : 
```bash
cd salary_aggregation_tg_bot
```

Creating a docker image
```bash
docker build . --tag tg_salary_bot
```

Running docker image
```bash
docker run -e BOT_TOKEN="<YOUR_BOT_TOKEN>" -e MONGODB_CONNECTION_STRING="<YOUR_MONGODB_CONNECTION_STRING>" -p 80:80 tg_salary_bot
```
