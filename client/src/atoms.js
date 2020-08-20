import { atom } from 'recoil'

export const activeDate = atom({
  key: 'activeDate',
  default: '2020-02-01',
})

export const theme = atom({
  key: 'theme',
  default: 'light',
})
