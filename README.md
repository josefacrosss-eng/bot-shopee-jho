on:
  schedule:
    - cron: '0 11 * * *' # 8h da manhã Brasil
jobs:
  bot:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: pip install requests
      - run: python bot.py
