import React from 'react'
import { useRecoilValue } from 'recoil'
import * as MuiStyles from '@material-ui/core/styles'
import * as Atoms from './atoms'

const createMuiTheme = MuiStyles.createMuiTheme
const { ThemeProvider: MuiThemeProvider } = MuiStyles

const muiTheme = createMuiTheme()
const lightTheme = {
  ...muiTheme,
  palette: {
    background: {
      default: '#FAFAFD',
    },
    primary: {
      main: '#FFFFFF',
    },
    secondary: {
      main: '#F9F9FD',
    } 
  }
}
const darkTheme = {
  ...muiTheme,
  palette: {
    background: {
      default: 'red',
    },
    primary: {
      main: '#FFFFFF',
    },
    secondary: {
      main: '#F9F9FD',
    } 
  }
}

export const ThemeProvider = ({ children }) => {
  const theme = useRecoilValue(Atoms.theme)
  console.log('ThemeProvider theme', theme)
  const activeTheme = theme === 'light' ? lightTheme : darkTheme
  const finalTheme = createMuiTheme(activeTheme)
  return <MuiThemeProvider theme={finalTheme}>{children}</MuiThemeProvider> 
}
