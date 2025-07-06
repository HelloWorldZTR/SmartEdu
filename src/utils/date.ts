import dayjs from 'dayjs'
import 'dayjs/locale/zh-cn'
import relativeTime from 'dayjs/plugin/relativeTime'

dayjs.extend(relativeTime)
dayjs.locale('zh-cn')

export const formatDate = (date: string | Date, format = 'YYYY-MM-DD'): string => {
  return dayjs(date).format(format)
}

export const formatRelativeTime = (date: string | Date): string => {
  return dayjs(date).fromNow()
}

export const isExpired = (date: string | Date): boolean => {
  return dayjs(date).isBefore(dayjs())
}

export const getDaysUntil = (date: string | Date): number => {
  return dayjs(date).diff(dayjs(), 'day')
} 