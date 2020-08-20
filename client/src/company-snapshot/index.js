import useSWR from 'swr'
import { activeDate } from '../atoms'
import { useRecoilValue } from 'recoil'

const API_URL = process.env.REACT_APP_API_URL
const COMPANY_SNAPSHOT_API_URL = `${API_URL}/stores/company-snapshot`

const fetcher = (...args) => fetch(...args).then(response => response.json())

export const useCompanySnapshotData = () => {
  const date = useRecoilValue(activeDate)
  let url = COMPANY_SNAPSHOT_API_URL
  if (date) {
    console.log('useCompanySnapshotData date', date, typeof(date))
    url += `?date=${date}`
  }
  console.log(' => url:', url)

  const { data, error } = useSWR(url, fetcher)
  return {
    data: data,
    isLoading: !error && !data,
    isError: error
  }
}
