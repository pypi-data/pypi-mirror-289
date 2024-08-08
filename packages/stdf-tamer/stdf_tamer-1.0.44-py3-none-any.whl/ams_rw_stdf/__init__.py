import construct #see docu at https://construct.readthedocs.io/en/latest/intro.html
from construct import this, Container
from struct import unpack, error
import sys


onechar = construct.PaddedString(1, "ascii")

FAR_payload = construct.Struct("CPU_TYPE" / construct.Const(b"\x02"),
                               "STDF_VER" / construct.Const(b"\x04"))

ATR_payload = construct.Struct("MOD_TIM"  / construct.Int32ul                                * "Date and time of STDF file modification",
                               "CMD_LINE" / construct.PascalString(construct.Byte, "ascii") * "Command line of program")


MIR_payload = construct.Struct("SETUP_T"  / construct.Int32ul                               * "Date and time of job setup",
                               "START_T"  / construct.Int32ul                               * "Date and time first part tested",
                               "STAT_NUM" / construct.Int8ul                                * "Tester station number",
                               "MODE_COD" / onechar                                         * "Test mode code (e.g. prod, dev) space",
                               "RTST_COD" / onechar                                         * "Lot retest code space",
                               "PROT_COD" / onechar                                         * "Data protection code space",
                               "BURN_TIM" / construct.Int16ul                               * "Burn-in time (in minutes) 65,535",
                               "CMOD_COD" / onechar                                         * "Command mode code space",
                               "LOT_ID"   / construct.PascalString(construct.Byte, "ascii") * "Lot ID (customer specified)",
                               "PART_TYP" / construct.PascalString(construct.Byte, "ascii") * "Part Type (or product ID)",
                               "NODE_NAM" / construct.PascalString(construct.Byte, "ascii") * "Name of node that generated data",
                               "TSTR_TYP" / construct.PascalString(construct.Byte, "ascii") * "Tester type",
                               "JOB_NAM"  / construct.PascalString(construct.Byte, "ascii") * "Job name (test program name)",
                               "JOB_REV"  / construct.PascalString(construct.Byte, "ascii") * "Job (test program) revision number length byte = 0",
                               "SBLOT_ID" / construct.PascalString(construct.Byte, "ascii") * "Sublot ID length byte = 0",
                               "OPER_NAM" / construct.PascalString(construct.Byte, "ascii") * "Operator name or ID (at setup time) length byte = 0",
                               "EXEC_TYP" / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Tester executive software type length byte = 0",
                               "EXEC_VER" / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Tester exec software version number length byte = 0",
                               "TEST_COD" / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Test phase or step code length byte = 0",
                               "TST_TEMP" / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Test temperature length byte = 0",
                               "USER_TXT" / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Generic user text length byte = 0",
                               "AUX_FILE" / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Name of auxiliary data file length byte = 0",
                               "PKG_TYP"  / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Package type length byte = 0",
                               "FAMLY_ID" / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Product family ID length byte = 0",
                               "DATE_COD" / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Date code length byte = 0",
                               "FACIL_ID" / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Test facility ID length byte = 0",
                               "FLOOR_ID" / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Test floor ID length byte = 0",
                               "PROC_ID"  / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Fabrication process ID length byte = 0",
                               "OPER_FRQ" / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Operation frequency or step length byte = 0",
                               "SPEC_NAM" / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Test specification name length byte = 0",
                               "SPEC_VER" / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Test specification version number length byte = 0",
                               "FLOW_ID"  / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Test flow ID length byte = 0",
                               "SETUP_ID" / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Test setup ID length byte = 0",
                               "DSGN_REV" / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Device design revision length byte = 0",
                               "ENG_ID"   / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Engineering lot ID length byte = 0",
                               "ROM_COD"  / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "ROM code ID length byte = 0",
                               "SERL_NUM" / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Tester serial number length byte = 0",
                               "SUPR_NAM" / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Supervisor name or ID length byte = 0")

SDR_payload = construct.Struct("HEAD_NUM"  /     construct.Int8ul                                     *  "Test head number",
                               "SITE_GRP"  /     construct.Int8ul                                     *  "Site group number",
                               "SITE_CNT"  /     construct.Int8ul                                     *  "Number (k) of test sites in site group",
                               "SITE_NUM"  /     construct.Array(this.SITE_CNT, construct.Int8ul)        *  "Array of test site numbers",
                               "HAND_TYP"  /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))     *  "Handler or prober type length byte = 0",
                               "HAND_ID"   /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))     *  "Handler or prober ID length byte = 0",
                               "CARD_TYP"  /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))     *  "Probe card type length byte = 0",
                               "CARD_ID"   /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))     *  "Probe card ID length byte = 0",
                               "LOAD_TYP"  /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))     *  "Load board type length byte = 0",
                               "LOAD_ID"   /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))     *  "Load board ID length byte = 0",
                               "DIB_TYP"   /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))     *  "DIB board type length byte = 0",
                               "DIB_ID"    /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))     *  "DIB board ID length byte = 0",
                               "CABL_TYP"  /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))     *  "Interface cable type length byte = 0",
                               "CABL_ID"   /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))     *  "Interface cable ID length byte = 0",
                               "CONT_TYP"  /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))     *  "Handler contactor type length byte = 0",
                               "CONT_ID"   /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))     *  "Handler contactor ID length byte = 0",
                               "LASR_TYP"  /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))     *  "Laser type length byte = 0",
                               "LASR_ID"   /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))     *  "Laser ID length byte = 0",
                               "EXTR_TYP"  /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))     *  "Extra equipment type field length byte = 0",
                               "EXTR_ID"   /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))     *  "Extra equipment ID length byte = 0")

PMR_payload = construct.Struct("PMR_INDX"  /  construct.Int16ul                                                 * "Unique index associated with pin",
                               "CHAN_TYP"  /  construct.Int16ul                                                 * "Channel type 0",
                               "CHAN_NAM"  /  construct.PascalString(construct.Byte, "ascii")                    * "Channel name length byte = 0",
                               "PHY_NAM"   /  construct.PascalString(construct.Byte, "ascii")                    * "Physical name of pin length byte = 0",
                               "LOG_NAM"   /  construct.PascalString(construct.Byte, "ascii")                    * "Logical name of pin length byte = 0",
                               "HEAD_NUM"  /  construct.Int8ul                                                    * "Head number associated with channel 1",
                               "SITE_NUM"  /  construct.Int8ul                                                    * "Site number associated with channel 1")

PGR_payload = construct.Struct("GRP_INDX" /      construct.Int16ul                                              *  "Unique index associated with pin group",
                               "GRP_NAM"  /      construct.PascalString(construct.Byte, "ascii")                 *  "Name of pin group length byte = 0",
                               "INDX_CNT" /      construct.Int16ul                                              *  "Count (k) of PMR indexes",
                               "PMR_INDX" /      construct.Array(this.INDX_CNT, construct.Int16ul) *  "Array of indexes for pins in the group INDX_CNT = 0)")

WCR_payload = construct.Struct("WAFR_SIZ"   / construct.Optional(construct.Float32l)              * "Diameter of wafer in WF_UNITS 0",
                               "DIE_HT"     / construct.Optional(construct.Float32l)              * "Height of die in WF_UNITS 0",
                               "DIE_WID"    / construct.Optional(construct.Float32l)              * "Width of die in WF_UNITS 0",
                               "WF_UNITS"   / construct.Optional(construct.Int8ul)                * "Units for wafer and die dimensions 0",
                               "WF_FLAT"    / construct.Optional(onechar)                  * "Orientation of wafer flat space",
                               "CENTER_X"   / construct.Optional(construct.Int16sl)               * "X coordinate of center die on wafer -32768",
                               "CENTER_Y"   / construct.Optional(construct.Int16sl)               * "Y coordinate of center die on wafer -32768",
                               "POS_X"      / construct.Optional(onechar)                  * "Positive X direction of wafer space",
                               "POS_Y"      / construct.Optional(onechar)                  * "Positive Y direction of wafer space")


# At this record... we encounter an issue
# Some of the STDFs we encounter interpret the bits 6/7 of the opt flag in a way which apears
# to be in disagreement of how the specification is written.
# Hence the change... We are thinking about how to solve this long term...
PTR_payload = construct.Struct("TEST_NUM"  /   construct.Int32ul                                                                               * "Test number",
                               "HEAD_NUM"  /   construct.Int8ul                                                                                  * "Test head number",
                               "SITE_NUM"  /   construct.Int8ul                                                                                  * "Test site number",
                               "TEST_FLG"  /   construct.Byte                                                                                  * "Test flags (fail, alarm, etc.)",
                               "PARM_FLG"  /   construct.Byte                                                                                  * "Parametric test flags (drift, etc.)",
                               "RESULT"    /   construct.Optional(construct.If((0 == this.TEST_FLG & 0x01), construct.Float32l))                                                                              * "Test result TEST_FLG bit 1 = 1",
                               "TEST_TXT"  /   construct.Optional(construct.PascalString(construct.Byte, "ascii"))                                                 * "Test description text or label length byte = 0",
                               "ALARM_ID"  /   construct.Optional(construct.PascalString(construct.Byte, "ascii"))                                                 * "Name of alarm length byte = 0",
                               "OPT_FLAG"  /   construct.Optional(construct.Byte)                                                              * "Optional data flag See note",
                               "RES_SCAL"  /   construct.Optional(construct.If((0 == this.OPT_FLAG & 0b00000001), construct.Int8sl))    * "Test results scaling exponent OPT_FLAG bit 0 = 1",
                               "LLM_SCAL"  /   construct.Optional(construct.If((0 == this.OPT_FLAG & 0b00010000), construct.Int8sl))    * "Low limit scaling exponent OPT_FLAG bit 4 or 6 = 1",
                               "HLM_SCAL"  /   construct.Optional(construct.If((0 == this.OPT_FLAG & 0b00100000), construct.Int8sl))    * "High limit scaling exponent OPT_FLAG bit 5 or 7 = 1",
                               "LO_LIMIT"  /   construct.Optional(construct.If((0 == this.OPT_FLAG & 0b00010000), construct.Float32l))  * "Low test limit value OPT_FLAG bit 4 or 6 = 1",
                               "HI_LIMIT"  /   construct.Optional(construct.If((0 == this.OPT_FLAG & 0b00100000), construct.Float32l))  * "High test limit value OPT_FLAG bit 5 or 7 = 1",
                               "UNITS"     /   construct.Optional(construct.PascalString(construct.Byte, "ascii"))                             * "Test units length byte = 0",
                               "C_RESFMT"  /   construct.Optional(construct.PascalString(construct.Byte, "ascii"))                             * "ANSI C result format string length byte = 0",
                               "C_LLMFMT"  /   construct.Optional(construct.PascalString(construct.Byte, "ascii"))                             * "ANSI C low limit format string length byte = 0",
                               "C_HLMFMT"  /   construct.Optional(construct.PascalString(construct.Byte, "ascii"))                             * "ANSI C high limit format string length byte = 0",
                               "LO_SPEC"   /   construct.Optional(construct.If((0 == this.OPT_FLAG & 0b00000100), construct.Float32l))           * "Low specification limit value OPT_FLAG bit 2 = 1",
                               "HI_SPEC"   /   construct.Optional(construct.If((0 == this.OPT_FLAG & 0b00001000), construct.Float32l))           * "High specification limit value OPT_FLAG bit 3 = 1")

#this is for speedy conversions to xlsx/parquet etc..
PTR_payload_reduced = construct.Struct("TEST_NUM"  /   construct.Int32ul                                                                               * "Test number",
                                       "HEAD_NUM"  /   construct.Int8ul                                                                                  * "Test head number",
                                       "SITE_NUM"  /   construct.Int8ul                                                                                  * "Test site number",
                                       "TEST_FLG"  /   construct.Byte                                                                                  * "Test flags (fail, alarm, etc.)",
                                       "PARM_FLG"  /   construct.Byte                                                                                  * "Parametric test flags (drift, etc.)",
                                       "RESULT"    /   construct.Optional(construct.If((0 == this.TEST_FLG & 0x01), construct.Float32l))                                                                              * "Test result TEST_FLG bit 1 = 1",
                                       "TEST_TXT"  /   construct.Optional(construct.PascalString(construct.Byte, "ascii"))                                                 * "Test description text or label length byte = 0",
                                       "ALARM_ID"  /   construct.Optional(construct.PascalString(construct.Byte, "ascii"))                                                 * "Name of alarm length byte = 0",
                                       "OPT_FLAG"  /   construct.Optional(construct.Byte)                                                              * "Optional data flag See note",
                                       "RES_SCAL"  /   construct.Optional(construct.If((0 == this.OPT_FLAG & 0b00000001), construct.Int8sl))    * "Test results scaling exponent OPT_FLAG bit 0 = 1",
                                       "LLM_SCAL"  /   construct.Optional(construct.If((0 == this.OPT_FLAG & 0b00010000), construct.Int8sl))    * "Low limit scaling exponent OPT_FLAG bit 4 or 6 = 1",
                                       "HLM_SCAL"  /   construct.Optional(construct.If((0 == this.OPT_FLAG & 0b00100000), construct.Int8sl))    * "High limit scaling exponent OPT_FLAG bit 5 or 7 = 1",
                                       "LO_LIMIT"  /   construct.Optional(construct.If((0 == this.OPT_FLAG & 0b00010000), construct.Float32l))  * "Low test limit value OPT_FLAG bit 4 or 6 = 1",
                                       "HI_LIMIT"  /   construct.Optional(construct.If((0 == this.OPT_FLAG & 0b00100000), construct.Float32l))  * "High test limit value OPT_FLAG bit 5 or 7 = 1")

MPR_payload = construct.Struct( "TEST_NUM"    / construct.Int32ul                                                                       * "Test number",
                                "HEAD_NUM"    / construct.Int8ul                                                                        * "Test head number",
                                "SITE_NUM"    / construct.Int8ul                                                                        * "Test site number",
                                "TEST_FLG"    / construct.Byte                                                                          * "Test flags (fail, alarm, etc.)",
                                "PARM_FLG"    / construct.Byte                                                                          * "Parametric test flags (drift, etc.)",
                                "RTN_ICNT"    / construct.Int16ul                                                                       * "Count (j) of PMR indexes See note",
                                "RSLT_CNT"    / construct.Int16ul                                                                       * "Count (k) of returned results See note",
                                "RTN_STAT"    / construct.Array(this.RTN_ICNT//2+this.RTN_ICNT%2, construct.Byte)                       * "Array of returned states RTN_ICNT = 0",
                                "RTN_RSLT"    / construct.Array(this.RSLT_CNT, construct.Float32l)                                      * "Array of returned results RSLT_CNT = 0",
                                "TEST_TXT"    / construct.Optional(construct.PascalString(construct.Byte, "ascii"))                     * "Descriptive text or label length byte = 0",
                                "ALARM_ID"    / construct.Optional(construct.PascalString(construct.Byte, "ascii"))                     * "Name of alarm length byte = 0",
                                "OPT_FLAG"    / construct.Optional(construct.Byte)                                                      * "Optional data flag See note",
                                "RES_SCAL"    / construct.Optional(construct.If((0 == this.OPT_FLAG & 0b00000001), construct.Int8sl))   * "Test result scaling exponent OPT_FLAG bit 0 = 1",
                                "LLM_SCAL"    / construct.Optional(construct.If((0 == this.OPT_FLAG & 0b00010000), construct.Int8sl))   * "Test low limit scaling exponent OPT_FLAG bit 4 or 6 = 1",
                                "HLM_SCAL"    / construct.Optional(construct.If((0 == this.OPT_FLAG & 0b00100000), construct.Int8sl))   * "Test high limit scaling exponent OPT_FLAG bit 5 or 7 = 1",
                                "LO_LIMIT"    / construct.Optional(construct.If((0 == this.OPT_FLAG & 0b00010000), construct.Float32l)) * "Test low limit value OPT_FLAG bit 4 or 6 = 1",
                                "HI_LIMIT"    / construct.Optional(construct.If((0 == this.OPT_FLAG & 0b00100000), construct.Float32l)) * "Test high limit value OPT_FLAG bit 5 or 7 = 1",
                                "START_IN"    / construct.Optional(construct.If((0 == this.TEST_FLG & 0x02), construct.Float32l))       * "Starting input value (condition) OPT_FLAG bit 1 = 1",
                                "INCR_IN"     / construct.Optional(construct.If((0 == this.TEST_FLG & 0x02), construct.Float32l))       * "Increment of input condition OPT_FLAG bit 1 = 1",
                                "RTN_INDX"    / construct.Optional(construct.If((0 != this.RTN_ICNT), construct.Array(this.RSLT_CNT, construct.Int16ul)))                                       * "Array of PMR indexes RTN_ICNT = 0",
                                "UNITS"       / construct.Optional(construct.PascalString(construct.Byte, "ascii"))                     * "Units of returned results length byte = 0",
                                "UNITS_IN"    / construct.Optional(construct.PascalString(construct.Byte, "ascii"))                     * "Input condition units length byte = 0",
                                "C_RESFMT"    / construct.Optional(construct.PascalString(construct.Byte, "ascii"))                     * "ANSI C result format string length byte = 0",
                                "C_LLMFMT"    / construct.Optional(construct.PascalString(construct.Byte, "ascii"))                     * "ANSI C low limit format string length byte = 0",
                                "C_HLMFMT"    / construct.Optional(construct.PascalString(construct.Byte, "ascii"))                     * "ANSI C high limit format string length byte = 0",
                                "LO_SPEC"     / construct.Optional(construct.If((0 == this.TEST_FLG & 0x04), construct.Float32l))       * "Low specification limit value OPT_FLAG bit 2 = 1",
                                "HI_SPEC"     / construct.Optional(construct.If((0 == this.TEST_FLG & 0x08), construct.Float32l))       * "High specification limit value OPT_FLAG bit 3 = 1")

FTR_payload = construct.Struct( "TEST_NUM"  /     construct.Int32ul                                                    *    "Test number",
                                "HEAD_NUM"  /     construct.Int8ul                                                     *     "Test head number",
                                "SITE_NUM"  /     construct.Int8ul                                                     *     "Test site number",
                                "TEST_FLG"  /     construct.Byte                                                       *       "Test flags (fail, alarm, etc.)",
                                "OPT_FLAG"  /     construct.Byte                                                       *       "Optional data flag See note",
                                "CYCL_CNT"  /     construct.Int32ul                                                    *    "Cycle count of vector OPT_FLAG bit 0 = 1",
                                "REL_VADR"  /     construct.Int32ul                                                    *    "Relative vector address OPT_FLAG bit 1 = 1",
                                "REPT_CNT"  /     construct.Int32ul                                                    *    "Repeat count of vector OPT_FLAG bit 2 = 1",
                                "NUM_FAIL"  /     construct.Int32ul                                                    *    "Number of pins with 1 or more failures OPT_FLAG bit 3 = 1",
                                "YFAIL_AD"  /     construct.Int32sl                                                    *    "Y logical device failure address OPT_FLAG bit 4 = 1",
                                "XFAIL_AD"  /     construct.Int32sl                                                    *    "X logical device failure address OPT_FLAG bit 4 = 1",
                                "VECT_OFF"  /     construct.Int16sl                                                    *    "Offset from vector of interest OPT_FLAG bit 5 = 1",
                                "RTN_ICNT"  /     construct.Int16ul                                                    *    "Count (j) of return data PMR indexes See note",
                                "PGM_ICNT"  /     construct.Int16ul                                                    *    "Count (k) of programmed state indexes See note",
                                "RTN_INDX"  /     construct.Array(this.RTN_ICNT, construct.Int16ul)                    * "Array of return data PMR indexes RTN_ICNT = 0",
                                "RTN_STAT"  /     construct.Array(this.RTN_ICNT//2+this.RTN_ICNT%2, construct.Byte)    * "Array of returned states RTN_ICNT = 0",
                                "PGM_INDX"  /     construct.Array(this.PGM_ICNT, construct.Int16ul)                    * "Array of programmed state indexes PGM_ICNT = 0",
                                "PGM_STAT"  /     construct.Array(this.PGM_ICNT//2+this.PGM_ICNT%2, construct.Byte)    * "Array of programmed states PGM_ICNT = 0",
                                "FAIL_PIN"  /     construct.Struct("bitFieldLength" / construct.Int16ul,
                                                                    "PL" / construct.Array(this.bitFieldLength//8 + (this.bitFieldLength%8!=0), construct.Byte)) *   "Failing pin bitfield length bytes = 0",
                                "VECT_NAM"  /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))  * "Vector module pattern name length byte = 0",
                                "TIME_SET"  /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))  * "Time set name length byte = 0",
                                "OP_CODE"   /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))  * "Vector Op Code length byte = 0",
                                "TEST_TXT"  /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))  * "Descriptive text or label length byte = 0",
                                "ALARM_ID"  /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))  * "Name of alarm length byte = 0",
                                "PROG_TXT"  /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))  * "Additional programmed information length byte = 0",
                                "RSLT_TXT"  /     construct.Optional(construct.PascalString(construct.Byte, "ascii"))  * "Additional result information length byte = 0",
                                "PATG_NUM"  /     construct.Int8ul                                                     *   "Pattern generator number 255",
                                "SPIN_MAP"  /     construct.Struct("bitFieldLength" / construct.Int16ul,
                                                                   "PL" / construct.Array(this.bitFieldLength//8 + (this.bitFieldLength%8!=0), construct.Byte)) *   "Bit map of enabled comparators length byte = 0",)

SBR_payload = construct.Struct("HEAD_NUM"  / construct.Int8ul                                * "Test head number See note",
                               "SITE_NUM"  / construct.Int8ul                                * "Test site number",
                               "SBIN_NUM"  / construct.Int16ul                               * "Software bin number",
                               "SBIN_CNT"  / construct.Int32ul                               * "Number of parts in bin",
                               "SBIN_PF"   / onechar                                         * "Pass/fail indication space",
                               "SBIN_NAM"  / construct.PascalString(construct.Byte, "ascii") * "Name of software bin length byte = 0")

HBR_payload = construct.Struct("HEAD_NUM"  / construct.Int8ul                                * "Test head number See note",
                               "SITE_NUM"  / construct.Int8ul                                * "Test site number",
                               "HBIN_NUM"  / construct.Int16ul                               * "Software bin number",
                               "HBIN_CNT"  / construct.Int32ul                               * "Number of parts in bin",
                               "HBIN_PF"   / onechar                                  * "Pass/fail indication space",
                               "HBIN_NAM"  / construct.PascalString(construct.Byte, "ascii") * "Name of software bin length byte = 0")

PCR_payload = construct.Struct("HEAD_NUM" / construct.Int8ul  * "Test head number See note",
                               "SITE_NUM" / construct.Int8ul  * "Test site number",
                               "PART_CNT" / construct.Int32ul * "Number of parts tested",
                               "RTST_CNT" / construct.Int32ul * "Number of parts retested 4,294,967,295",
                               "ABRT_CNT" / construct.Int32ul * "Number of aborts during testing 4,294,967,295",
                               "GOOD_CNT" / construct.Int32ul * "Number of good (passed) parts tested 4,294,967,295",
                               "FUNC_CNT" / construct.Int32ul * "Number of functional parts tested 4,294,967,295")

MRR_payload = construct.Struct("FINISH_T" / construct.Int32ul                               * "Date and time last part tested",
                               "DISP_COD" / onechar                                         * "Lot disposition code space",
                               "USR_DESC" / construct.PascalString(construct.Byte, "ascii") * "Lot description supplied by user length byte = 0",
                               "EXC_DESC" / construct.PascalString(construct.Byte, "ascii") * "Lot description supplied by exec length byte = 0")

WIR_payload = construct.Struct("HEAD_NUM" / construct.Int8ul                               * "Test head number",
                               "SITE_GRP" / construct.Int8ul                               * "Site group number",
                               "START_T" / construct.Int32ul                               * "Lot description supplied by user length byte = 0",
                               "WAFER_ID" / construct.PascalString(construct.Byte, "ascii") * "Waver ID")

PIR_payload =  construct.Struct( "HEAD_NUM" / construct.Int8ul                              *  "Test head number",
                                 "SITE_NUM" / construct.Int8ul                              *  "Test site number")

PRR_payload =  construct.Struct( "HEAD_NUM" / construct.Int8ul                               *  "Test head number",
                                 "SITE_NUM" / construct.Int8ul                               *  "Test site number",
                                 "PART_FLG" / construct.Int8ul                               *  "Part information flag",
                                 "NUM_TEST" / construct.Int16ul                              *  "Number of tests executed",
                                 "HARD_BIN" / construct.Int16ul                              *  "Hardware bin number",
                                 "SOFT_BIN" / construct.Int16ul                              *  "Software bin number 65535",
                                 "X_COORD"  / construct.Int16sl                              * "(Wafer) X coordinate -32768",
                                 "Y_COORD"  / construct.Int16sl                              * "(Wafer) Y coordinate -32768",
                                 "TEST_T"   / construct.Int32ul                              * "Elapsed test time in milliseconds 0",
                                 "PART_ID"  / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Part identification length byte = 0",
                                 "PART_TXT" / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Part description text length byte = 0",
                                 "PART_FIX" / construct.Optional(construct.PascalString(construct.Byte, "ascii")) * "Part repair information length byte = 0")

TSR_payload =  construct.Struct("HEAD_NUM" / construct.Int8ul    *                            "Test head number See note",
                                "SITE_NUM" / construct.Int8ul    *                            "Test site number",
                                "TEST_TYP" / onechar           *                            "Test type space",
                                "TEST_NUM" / construct.Int32ul *                            " Test number",
                                "EXEC_CNT" / construct.Int32ul *                            " Number of test executions 4,294,967,295",
                                "FAIL_CNT" / construct.Int32ul *                            " Number of test failures 4,294,967,295",
                                "ALRM_CNT" / construct.Int32ul *                            " Number of alarmed tests 4,294,967,295",
                                "TEST_NAM" / construct.PascalString(construct.Byte, "ascii") * "Test name length byte = 0",
                                "SEQ_NAME" / construct.PascalString(construct.Byte, "ascii") * "Sequencer (program segment/flow) name length byte = 0",
                                "TEST_LBL" / construct.PascalString(construct.Byte, "ascii") * "Test label or text length byte = 0",
                                "OPT_FLAG" / construct.Optional(construct.Byte)                                 * "Optional data flag See note",
                                "TEST_TIM" / construct.Optional(construct.If((0 == this.OPT_FLAG & 0x04),construct.Float32l))                             * " Average test execution time in seconds OPT_FLAG bit 2 = 1",
                                "TEST_MIN" / construct.Optional(construct.If((0 == this.OPT_FLAG & 0x01),construct.Float32l))                             * " Lowest test result value OPT_FLAG bit 0 = 1",
                                "TEST_MAX" / construct.Optional(construct.If((0 == this.OPT_FLAG & 0x02),construct.Float32l))                             * " Highest test result value OPT_FLAG bit 1 = 1",
                                "TST_SUMS" / construct.Optional(construct.If((0 == this.OPT_FLAG & 0x10),construct.Float32l))                             * " Sumof test result values OPT_FLAG bit 4 = 1",
                                "TST_SQRS" / construct.Optional(construct.If((0 == this.OPT_FLAG & 0x20),construct.Float32l))                             * " Sum of squares of test result values OPT_FLAG bit 5 = 1")


_dict_of_payloads  = {( 0<<8|10) :FAR_payload,
                      ( 0<<8|20) :ATR_payload,
                      ( 1<<8|10) :MIR_payload,
                      ( 1<<8|20) :MRR_payload,
                      ( 1<<8|80) :SDR_payload,
                      ( 1<<8|60) :PMR_payload,
                      ( 1<<8|62) :PGR_payload,
                      ( 1<<8|40) :HBR_payload,
                      ( 1<<8|50) :SBR_payload,
                      ( 1<<8|30) :PCR_payload,
                      ( 2<<8|30) :WCR_payload,
                      ( 2<<8|10) :WIR_payload,
                      ( 5<<8|10) :PIR_payload,
                      ( 5<<8|20) :PRR_payload,
                      (10<<8|30) :TSR_payload,
                      (15<<8|10) :PTR_payload,
                      (15<<8|15) :MPR_payload,
                      (15<<8|20) :FTR_payload
                      }

#this is for speedy conversions to xlsx/parquet etc..
_reduced_dict_of_payloads = {( 1<<8|10):MIR_payload,
                             ( 1<<8|60) :PMR_payload,
                             ( 5<<8|20):PRR_payload,
                             (15<<8|10):PTR_payload_reduced,
                             (15<<8|15) :MPR_payload,}


def calc_len_of_stdf_record(this):
    """"This function calculates the length of an stdf record
    
    by rendering the payload and then using the rendered paylod
    to count the bytes.
    
    This is suboptimal, as only one render process should be needed,
    and it makes it impossible to compile the generator.

    """
    this = dict(this)
    pl_construct = _dict_of_payloads[this["REC_TYP"]<<8|this["REC_SUB"]]
    return len(pl_construct.build(Container(this["PL"])))


RECORD = construct.Struct("REC_LEN"  / construct.Rebuild(construct.Int16ul, calc_len_of_stdf_record) * "Bytes of data following header",
                          "REC_TYP"  / construct.Int8ul    * "Record type (1)",
                          "REC_SUB"  / construct.Int8ul    * "Record sub-type (10)",
                          "PL"       / construct.Switch(this.REC_TYP<<8|this.REC_SUB, _dict_of_payloads))

compileable_RECORD = construct.Struct("REC_LEN"  / construct.Int16ul * "Bytes of data following header",
                                      "REC_TYP"  / construct.Int8ul    * "Record type (1)",
                                      "REC_SUB"  / construct.Int8ul    * "Record sub-type (10)",
                                      "PL"       / construct.Switch(this.REC_TYP<<8|this.REC_SUB, _dict_of_payloads))

#this is for speedy conversions to xlsx/parquet etc..
_compileable_RECORD_noLen_simplfified = construct.Struct("REC_TYP"  / construct.Int8ul    * "Record type (1)",
                                                        "REC_SUB"  / construct.Int8ul    * "Record sub-type (10)",
                                                        "PL"       / construct.Switch(this.REC_TYP<<8|this.REC_SUB, _reduced_dict_of_payloads))

def get_record_bytes(stream):
    """ only get the raw bytes

    This seperates the handling of the length field from the construct.
    The advantage is that all issues with one record, as long as the length field is correct,
    are isolated to this specific record, using these 3 easy to check lines.
    """

    length = stream.peek(2)
    try:
        len2Read = ((length[1]<<8)+length[0])+4
        buf = stream.read(len2Read)
        if len(buf)==len2Read:
            return buf
        raise EOFError("couldnt read record payload")
    except IndexError:
        pass
    length = stream.read(2)
    if len(length)!=2:
        raise EOFError("Couldnt read record length field")
    lengthOfPL = ((length[1]<<8)+length[0])+2
    pl = stream.read(lengthOfPL)
    if len(pl)==lengthOfPL:
        return length+pl
    raise EOFError("couldnt read length of record payload")


def records_no_length_simplified(iFile=sys.stdin):
    try:
        parser = _compileable_RECORD_noLen_simplfified.compile(containertype="dict")
    except TypeError:
        parser = _compileable_RECORD_noLen_simplfified.compile()
    while True:
        length = iFile.read(2)
        try:
            (length,) = unpack("H", length)
        except error:
            raise EOFError("Couldnt read length field of Record, unexpected end of STDF")
        yield parser.parse(iFile.read(length+2))


def parse_record(stream):
    """ This function parses in 2 stages.

    Get header and raw payload, then parse deeply from just this record.
    This way the REC_LEN field is driving the advancing in the stream.
    """
    length = stream.read(2)
    if not length:
        raise EOFError()
    data = length + stream.read(((length[1]<<8)+length[0])+2)
    return RECORD.parse(data)
