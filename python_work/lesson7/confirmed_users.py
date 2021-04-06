unconfirmed_users = ['alice', 'brian', 'candace']
confiremed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user：" + current_user.title())
    confiremed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confiremed_users:
    print(confirmed_user.title())
