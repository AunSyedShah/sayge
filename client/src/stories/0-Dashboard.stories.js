import React from 'react'
import { linkTo } from '@storybook/addon-links'
import Home from '../Home'

export default {
  title: 'Home',
  component: Home,
}

export const ToStorybook = () => <Home showApp={linkTo('Button')} />

ToStorybook.story = {
  name: 'to Storybook',
}
