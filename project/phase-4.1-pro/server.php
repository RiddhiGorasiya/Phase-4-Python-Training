<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $action = $_POST['action'];
    $email = $_POST['email'];
    $password = $_POST['password'];

    if ($action == "login") {
        // Simple check (replace with DB check)
        if ($email == "test@test.com" && $password == "1234") {
            echo "Login Successful!";
        } else {
            echo "Invalid credentials!";
        }
    }

    if ($action == "signup") {
        $username = $_POST['username'];
        // Save to DB (demo only)
        echo "Signup Successful for $username!";
    }
}
?>
