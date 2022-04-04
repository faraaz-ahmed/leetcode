def solve(n, dice):
  dice.sort()
  count = 0
  for i in range(0, n):
    if count < dice[i]:
      count += 1
  print(count)

t = int(input())
for i in range(0, t):
  n = int(input())
  dice = list(map(int, input().split()))
  print("Case #" + str(i + 1) + ':')
  solve(n, dice)

  #wrong
  #
  # int n;
  # cin>>n;
  # vector <int> v(n);
  # for(int i = 0; i< n; i++) {
  #   cin >> v[i];
  # }
  # sort(v.begin(), v.end());
  # for( auto x:v) {
  #   if (x >= ans)
  #     ans += 1;
  # }
  # ans -= 1;
  # cout<<ans<<endl;