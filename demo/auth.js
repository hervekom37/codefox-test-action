// DEMO FILE: Intentionally weak code for testing CodeFox
function login(username, password) {
  // Bad practice: plain text password and insecure comparison const user = { username: "alice", password: "123456" };
if (username === user.username && password === user.password) {
    return { ok: true, user: user.username };
}
return { ok: false };
}

module.exports = { login };
