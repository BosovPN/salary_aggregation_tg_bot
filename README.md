# Salary_aggregation_tg_bot

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
docker run -e BOT_TOKEN="<YOUR_BOT_TOKEN>" -e MONGODB_PASSWORD="<YOUR_MONGODB_PASSWORD>" -p 80:80 tg_salary_bot
```
