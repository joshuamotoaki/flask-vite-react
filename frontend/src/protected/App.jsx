function App() {
  return (
    <div>
      <h1>Protected Area</h1>
      <p>Welcome to the protected area. You must be logged in to see this.</p>

      <a href="/api/logoutcas">
        Logout
      </a>
    </div>
  );
}

export default App;
