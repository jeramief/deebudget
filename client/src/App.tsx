import {useMemo} from "react";
import {createTheme} from "@mui/material/styles";
import {themeSettings} from "./theme";
import {Box, CssBaseline, ThemeProvider} from "@mui/material";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Navbar from "@/components/Navbar";
import Dashboard from "@/scenes/dashboard";
import Predictions from "@/scenes/predictions"

function App() {
  const theme = useMemo(() => createTheme(themeSettings), [])
  return <div className="app">
    <BrowserRouter>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <Box height="100%" width="100%" padding="1rem 2rem 4rem">
          <Navbar />
          <Routes>
            <Route
              path="/"
              element={<Dashboard />}
            />
            <Route
              path="/predictions"
              element={<Predictions />}
            />
          </Routes>
        </Box>
      </ThemeProvider>
    </BrowserRouter>
  </div>
}

export default App
