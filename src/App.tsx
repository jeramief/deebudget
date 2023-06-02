import {useMemo} from "react";
import {createTheme} from "@mui/material/styles";
import {themeSettings} from "@/theme.ts";
import {Box, CssBaseline, ThemeProvider} from "@mui/material";

function App() {
  const theme = useMemo(() => createTheme(themeSettings), [])
  return <div className="app">
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Box height="100%" width="100%" padding="1rem 2rem 4rem">

      </Box>
    </ThemeProvider>
  </div>
}

export default App
