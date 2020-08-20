import React from 'react'
import { useRecoilState } from 'recoil'
import Switch from '@material-ui/core/Switch'
import FormGroup from '@material-ui/core/FormGroup'
import FormControlLabel from '@material-ui/core/FormControlLabel'
import FormControl from '@material-ui/core/FormControl'
import { theme } from './atoms'

export default () => {
  const [activeTheme, setActiveTheme] = useRecoilState(theme)

  const onChange = (event) => {
    console.log('onChange event', event.target.checked, activeTheme)
    setActiveTheme(event.target.checked === true ? 'dark' : 'light')
  }

  return (
    <FormControl component="fieldset">
      <FormGroup aria-label="position" row>
        <FormControlLabel
          onChange={onChange}
          control={<Switch color="primary" />}
          label="Dark Mode"
          labelPlacement="start"
        />
      </FormGroup>
    </FormControl>
  )
}
