# Copyright 2023-2024 Geoffrey R. Scheller
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Useful modules I found difficult to implement in a strictly typed manner.

## Modules

### module `grscheller.untyped.nothing`

#### class `Nothing()`

Class representing a non-existent value.

* Nothing() is a singleton
* Nothing() instances should be compared with the `is` operator, not `==`
* my[py] becomes problematic when module is strictly typed
  * implementing the module becomes vastly more complicated
  * in client code my[py] keeps warning you about what you are doing
  * maybe using `Any` in this use case is not a bad thing

#### instance variable: `nothing`

* nothing = Nothing() is a singleton

---

"""
__version__ = "0.1.0"
__author__ = "Geoffrey R. Scheller"
__copyright__ = "Copyright (c) 2024 Geoffrey R. Scheller"
__license__ = "Apache License 2.0"
