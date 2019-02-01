class Message < ApplicationRecord
  scope :unprinted, -> { where(printed: false) }
end
