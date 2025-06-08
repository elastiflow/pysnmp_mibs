# SNMP MIB module (CEM-COMMON-PROCESSOR) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-COMMON-PROCESSOR.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:21 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(catena,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "catena")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cnCommonProcessorModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 7)
)
if mibBuilder.loadTexts:
    cnCommonProcessorModule.setRevisions(
        ("2002-03-11 09:29",
         "2003-10-17 13:44")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CnCPProcessorType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("m860", 1),
          ("m8260", 2),
          ("modec1a", 3),
          ("modec1b", 4),
          ("modec1c", 5))
    )



class CnCCCardType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              35,
              37,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("cec", 0),
          ("t1c", 1),
          ("oc3EnhancedShorthaul", 2),
          ("oc3EnhancedLonghaul", 3),
          ("oc3Shorthaul", 4),
          ("oc3Longhaul", 5),
          ("adslLine", 6),
          ("alarmAndTest", 7),
          ("hydraLine", 8),
          ("opticalLine", 9),
          ("feature", 10),
          ("opticalInterface", 11),
          ("catenaChannelUnit", 12),
          ("legacyChannelUnit", 13),
          ("oc12Wan", 14),
          ("ds3Wan", 15),
          ("opticNetworkTermination", 35),
          ("e1", 37),
          ("unknown", 9999))
    )



class CnCPBanks(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("bankA", 1),
          ("bankB", 2))
    )



class CnCPActiveBankControlType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cnCPToggleToBank1Succeeded", 1),
          ("cnCPToggleToBank2Succeeded", 2),
          ("cnCPToggleToBank1Failed", 3),
          ("cnCPToggleToBank2Failed", 4),
          ("cnCPToggleActiveBank", 5),
          ("cnCPToggleInactiveBank", 6))
    )



class CnCPProcessorStatisticsType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cnProcessorFirst15MinStats", 1),
          ("cnProcessorSecond15MinStats", 2),
          ("cnProcessorThird15MinStats", 3),
          ("cnProcessorFourth15MinStats", 4),
          ("cnProcessorFourthLast15MinStats", 5),
          ("cnProcessorThirdLast15MinStats", 6),
          ("cnProcessorSecondLast15MinStats", 7),
          ("cnProcessorLast15MinStats", 8))
    )



class CnCardStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cardNotThere", 1),
          ("cardInitializing", 2),
          ("cardActiveJoined", 3),
          ("cardActivePartitioned", 4),
          ("cardInactiveJoined", 5),
          ("cardInactivePartitioned", 6))
    )



class CnCPStatisticsReset(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("triggerReset", 1),
          ("resetSuccess", 2),
          ("resetFailed", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CnCommonProcessorTable_Object = MibTable
cnCommonProcessorTable = _CnCommonProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 2)
)
if mibBuilder.loadTexts:
    cnCommonProcessorTable.setStatus("obsolete")
_CnCommonProcessorEntry_Object = MibTableRow
cnCommonProcessorEntry = _CnCommonProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 2, 1)
)
cnCommonProcessorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cnCommonProcessorEntry.setStatus("obsolete")
_CnCPProcessorType_Type = CnCPProcessorType
_CnCPProcessorType_Object = MibTableColumn
cnCPProcessorType = _CnCPProcessorType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 2, 1, 2),
    _CnCPProcessorType_Type()
)
cnCPProcessorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPProcessorType.setStatus("obsolete")


class _CnCPProcessorAndSpeedInMHz_Type(CnCPProcessorType):
    """Custom type cnCPProcessorAndSpeedInMHz based on CnCPProcessorType"""
    subtypeSpec = CnCPProcessorType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_CnCPProcessorAndSpeedInMHz_Type.__name__ = "CnCPProcessorType"
_CnCPProcessorAndSpeedInMHz_Object = MibTableColumn
cnCPProcessorAndSpeedInMHz = _CnCPProcessorAndSpeedInMHz_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 2, 1, 3),
    _CnCPProcessorAndSpeedInMHz_Type()
)
cnCPProcessorAndSpeedInMHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPProcessorAndSpeedInMHz.setStatus("obsolete")
_CnCPRAMinMBytes_Type = Integer32
_CnCPRAMinMBytes_Object = MibTableColumn
cnCPRAMinMBytes = _CnCPRAMinMBytes_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 2, 1, 4),
    _CnCPRAMinMBytes_Type()
)
cnCPRAMinMBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPRAMinMBytes.setStatus("obsolete")


class _CnCPProcessorUtilization_Type(Integer32):
    """Custom type cnCPProcessorUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CnCPProcessorUtilization_Type.__name__ = "Integer32"
_CnCPProcessorUtilization_Object = MibTableColumn
cnCPProcessorUtilization = _CnCPProcessorUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 2, 1, 5),
    _CnCPProcessorUtilization_Type()
)
cnCPProcessorUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPProcessorUtilization.setStatus("obsolete")
if mibBuilder.loadTexts:
    cnCPProcessorUtilization.setUnits("%")
_CnCPCurrentProcessorFreeMemory_Type = Integer32
_CnCPCurrentProcessorFreeMemory_Object = MibTableColumn
cnCPCurrentProcessorFreeMemory = _CnCPCurrentProcessorFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 2, 1, 6),
    _CnCPCurrentProcessorFreeMemory_Type()
)
cnCPCurrentProcessorFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPCurrentProcessorFreeMemory.setStatus("obsolete")
if mibBuilder.loadTexts:
    cnCPCurrentProcessorFreeMemory.setUnits("bytes")
_CnCPCurrentProcessorLargestAvailableMemoryFragment_Type = Integer32
_CnCPCurrentProcessorLargestAvailableMemoryFragment_Object = MibTableColumn
cnCPCurrentProcessorLargestAvailableMemoryFragment = _CnCPCurrentProcessorLargestAvailableMemoryFragment_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 2, 1, 7),
    _CnCPCurrentProcessorLargestAvailableMemoryFragment_Type()
)
cnCPCurrentProcessorLargestAvailableMemoryFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPCurrentProcessorLargestAvailableMemoryFragment.setStatus("obsolete")
if mibBuilder.loadTexts:
    cnCPCurrentProcessorLargestAvailableMemoryFragment.setUnits("bytes")
_CnCPShelfNumber_Type = Integer32
_CnCPShelfNumber_Object = MibTableColumn
cnCPShelfNumber = _CnCPShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 2, 1, 8),
    _CnCPShelfNumber_Type()
)
cnCPShelfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPShelfNumber.setStatus("obsolete")
_CnCPSlotNumber_Type = Integer32
_CnCPSlotNumber_Object = MibTableColumn
cnCPSlotNumber = _CnCPSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 2, 1, 9),
    _CnCPSlotNumber_Type()
)
cnCPSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPSlotNumber.setStatus("obsolete")
_CnCPCardType_Type = CnCCCardType
_CnCPCardType_Object = MibTableColumn
cnCPCardType = _CnCPCardType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 2, 1, 10),
    _CnCPCardType_Type()
)
cnCPCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPCardType.setStatus("obsolete")
_CnCommonProcessorBootBankTable_Object = MibTable
cnCommonProcessorBootBankTable = _CnCommonProcessorBootBankTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4)
)
if mibBuilder.loadTexts:
    cnCommonProcessorBootBankTable.setStatus("current")
_CnCommonProcessorBootBankEntry_Object = MibTableRow
cnCommonProcessorBootBankEntry = _CnCommonProcessorBootBankEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4, 1)
)
cnCommonProcessorBootBankEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cnCommonProcessorBootBankEntry.setStatus("current")


class _CnCPFirmwareImageName_Type(OctetString):
    """Custom type cnCPFirmwareImageName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnCPFirmwareImageName_Type.__name__ = "OctetString"
_CnCPFirmwareImageName_Object = MibTableColumn
cnCPFirmwareImageName = _CnCPFirmwareImageName_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4, 1, 1),
    _CnCPFirmwareImageName_Type()
)
cnCPFirmwareImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPFirmwareImageName.setStatus("current")
_CnCPFirmwareSize_Type = Integer32
_CnCPFirmwareSize_Object = MibTableColumn
cnCPFirmwareSize = _CnCPFirmwareSize_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4, 1, 2),
    _CnCPFirmwareSize_Type()
)
cnCPFirmwareSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPFirmwareSize.setStatus("current")
_CnCPFirmwareBuildDate_Type = DateAndTime
_CnCPFirmwareBuildDate_Object = MibTableColumn
cnCPFirmwareBuildDate = _CnCPFirmwareBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4, 1, 3),
    _CnCPFirmwareBuildDate_Type()
)
cnCPFirmwareBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPFirmwareBuildDate.setStatus("current")
_CnCPFirmwareDateWritten_Type = DateAndTime
_CnCPFirmwareDateWritten_Object = MibTableColumn
cnCPFirmwareDateWritten = _CnCPFirmwareDateWritten_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4, 1, 4),
    _CnCPFirmwareDateWritten_Type()
)
cnCPFirmwareDateWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPFirmwareDateWritten.setStatus("current")


class _CnCPBankAImageName_Type(OctetString):
    """Custom type cnCPBankAImageName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnCPBankAImageName_Type.__name__ = "OctetString"
_CnCPBankAImageName_Object = MibTableColumn
cnCPBankAImageName = _CnCPBankAImageName_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4, 1, 5),
    _CnCPBankAImageName_Type()
)
cnCPBankAImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPBankAImageName.setStatus("current")
_CnCPBankASize_Type = Integer32
_CnCPBankASize_Object = MibTableColumn
cnCPBankASize = _CnCPBankASize_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4, 1, 6),
    _CnCPBankASize_Type()
)
cnCPBankASize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPBankASize.setStatus("current")
_CnCPBankABuildDate_Type = DateAndTime
_CnCPBankABuildDate_Object = MibTableColumn
cnCPBankABuildDate = _CnCPBankABuildDate_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4, 1, 7),
    _CnCPBankABuildDate_Type()
)
cnCPBankABuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPBankABuildDate.setStatus("current")
_CnCPBankADateWritten_Type = DateAndTime
_CnCPBankADateWritten_Object = MibTableColumn
cnCPBankADateWritten = _CnCPBankADateWritten_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4, 1, 8),
    _CnCPBankADateWritten_Type()
)
cnCPBankADateWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPBankADateWritten.setStatus("current")


class _CnCPBankBImageName_Type(OctetString):
    """Custom type cnCPBankBImageName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnCPBankBImageName_Type.__name__ = "OctetString"
_CnCPBankBImageName_Object = MibTableColumn
cnCPBankBImageName = _CnCPBankBImageName_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4, 1, 9),
    _CnCPBankBImageName_Type()
)
cnCPBankBImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPBankBImageName.setStatus("current")
_CnCPBankBSize_Type = Integer32
_CnCPBankBSize_Object = MibTableColumn
cnCPBankBSize = _CnCPBankBSize_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4, 1, 10),
    _CnCPBankBSize_Type()
)
cnCPBankBSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPBankBSize.setStatus("current")
_CnCPBankBBuildDate_Type = DateAndTime
_CnCPBankBBuildDate_Object = MibTableColumn
cnCPBankBBuildDate = _CnCPBankBBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4, 1, 11),
    _CnCPBankBBuildDate_Type()
)
cnCPBankBBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPBankBBuildDate.setStatus("current")
_CnCPBankBDateWritten_Type = DateAndTime
_CnCPBankBDateWritten_Object = MibTableColumn
cnCPBankBDateWritten = _CnCPBankBDateWritten_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4, 1, 12),
    _CnCPBankBDateWritten_Type()
)
cnCPBankBDateWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPBankBDateWritten.setStatus("current")
_CnCPNextBootBank_Type = CnCPBanks
_CnCPNextBootBank_Object = MibTableColumn
cnCPNextBootBank = _CnCPNextBootBank_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4, 1, 13),
    _CnCPNextBootBank_Type()
)
cnCPNextBootBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPNextBootBank.setStatus("current")
_CnCPActiveBootBank_Type = CnCPBanks
_CnCPActiveBootBank_Object = MibTableColumn
cnCPActiveBootBank = _CnCPActiveBootBank_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4, 1, 14),
    _CnCPActiveBootBank_Type()
)
cnCPActiveBootBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPActiveBootBank.setStatus("current")
_CnCPActiveBankControl_Type = CnCPActiveBankControlType
_CnCPActiveBankControl_Object = MibTableColumn
cnCPActiveBankControl = _CnCPActiveBankControl_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4, 1, 15),
    _CnCPActiveBankControl_Type()
)
cnCPActiveBankControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnCPActiveBankControl.setStatus("current")
_CnCPBootBankCardType_Type = CnCCCardType
_CnCPBootBankCardType_Object = MibTableColumn
cnCPBootBankCardType = _CnCPBootBankCardType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4, 1, 16),
    _CnCPBootBankCardType_Type()
)
cnCPBootBankCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnCPBootBankCardType.setStatus("current")
_CnCPBootBankShelfNumber_Type = Integer32
_CnCPBootBankShelfNumber_Object = MibTableColumn
cnCPBootBankShelfNumber = _CnCPBootBankShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4, 1, 17),
    _CnCPBootBankShelfNumber_Type()
)
cnCPBootBankShelfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPBootBankShelfNumber.setStatus("current")
_CnCPBootBankSlotNumber_Type = Integer32
_CnCPBootBankSlotNumber_Object = MibTableColumn
cnCPBootBankSlotNumber = _CnCPBootBankSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 4, 1, 18),
    _CnCPBootBankSlotNumber_Type()
)
cnCPBootBankSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPBootBankSlotNumber.setStatus("current")
_CnCommonProcessorStatisticsTable_Object = MibTable
cnCommonProcessorStatisticsTable = _CnCommonProcessorStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 5)
)
if mibBuilder.loadTexts:
    cnCommonProcessorStatisticsTable.setStatus("obsolete")
_CnCommonProcessorStatisticsEntry_Object = MibTableRow
cnCommonProcessorStatisticsEntry = _CnCommonProcessorStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 5, 1)
)
cnCommonProcessorStatisticsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CEM-COMMON-PROCESSOR", "cnCPIntervalProcessorStatisticsType"),
)
if mibBuilder.loadTexts:
    cnCommonProcessorStatisticsEntry.setStatus("obsolete")
_CnCPIntervalProcessorStatisticsType_Type = CnCPProcessorStatisticsType
_CnCPIntervalProcessorStatisticsType_Object = MibTableColumn
cnCPIntervalProcessorStatisticsType = _CnCPIntervalProcessorStatisticsType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 5, 1, 1),
    _CnCPIntervalProcessorStatisticsType_Type()
)
cnCPIntervalProcessorStatisticsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPIntervalProcessorStatisticsType.setStatus("obsolete")
_CnCPProcessorStatisticsIntervalIndex_Type = Gauge32
_CnCPProcessorStatisticsIntervalIndex_Object = MibTableColumn
cnCPProcessorStatisticsIntervalIndex = _CnCPProcessorStatisticsIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 5, 1, 2),
    _CnCPProcessorStatisticsIntervalIndex_Type()
)
cnCPProcessorStatisticsIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPProcessorStatisticsIntervalIndex.setStatus("obsolete")
_CnCPIntervalProcessorFreeMemory_Type = Integer32
_CnCPIntervalProcessorFreeMemory_Object = MibTableColumn
cnCPIntervalProcessorFreeMemory = _CnCPIntervalProcessorFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 5, 1, 3),
    _CnCPIntervalProcessorFreeMemory_Type()
)
cnCPIntervalProcessorFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPIntervalProcessorFreeMemory.setStatus("obsolete")
if mibBuilder.loadTexts:
    cnCPIntervalProcessorFreeMemory.setUnits("bytes")
_CnCPIntervalProcessorLargestAvailableMemoryFragment_Type = Integer32
_CnCPIntervalProcessorLargestAvailableMemoryFragment_Object = MibTableColumn
cnCPIntervalProcessorLargestAvailableMemoryFragment = _CnCPIntervalProcessorLargestAvailableMemoryFragment_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 5, 1, 4),
    _CnCPIntervalProcessorLargestAvailableMemoryFragment_Type()
)
cnCPIntervalProcessorLargestAvailableMemoryFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPIntervalProcessorLargestAvailableMemoryFragment.setStatus("obsolete")
_CnCPCardTypeStatistics_Type = CnCCCardType
_CnCPCardTypeStatistics_Object = MibTableColumn
cnCPCardTypeStatistics = _CnCPCardTypeStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 5, 1, 5),
    _CnCPCardTypeStatistics_Type()
)
cnCPCardTypeStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPCardTypeStatistics.setStatus("obsolete")
_CnCommonProcessorLVDSStatisticsTable_Object = MibTable
cnCommonProcessorLVDSStatisticsTable = _CnCommonProcessorLVDSStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 6)
)
if mibBuilder.loadTexts:
    cnCommonProcessorLVDSStatisticsTable.setStatus("obsolete")
_CnCommonProcessorLVDSStatisticsEntry_Object = MibTableRow
cnCommonProcessorLVDSStatisticsEntry = _CnCommonProcessorLVDSStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 6, 1)
)
cnCommonProcessorLVDSStatisticsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cnCommonProcessorLVDSStatisticsEntry.setStatus("obsolete")


class _CnCommonProcessorShelfStatisitcs_Type(Integer32):
    """Custom type cnCommonProcessorShelfStatisitcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CnCommonProcessorShelfStatisitcs_Type.__name__ = "Integer32"
_CnCommonProcessorShelfStatisitcs_Object = MibTableColumn
cnCommonProcessorShelfStatisitcs = _CnCommonProcessorShelfStatisitcs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 6, 1, 1),
    _CnCommonProcessorShelfStatisitcs_Type()
)
cnCommonProcessorShelfStatisitcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCommonProcessorShelfStatisitcs.setStatus("obsolete")


class _CnCommonProcessorSlotStatisitcs_Type(Integer32):
    """Custom type cnCommonProcessorSlotStatisitcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 47),
    )


_CnCommonProcessorSlotStatisitcs_Type.__name__ = "Integer32"
_CnCommonProcessorSlotStatisitcs_Object = MibTableColumn
cnCommonProcessorSlotStatisitcs = _CnCommonProcessorSlotStatisitcs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 6, 1, 2),
    _CnCommonProcessorSlotStatisitcs_Type()
)
cnCommonProcessorSlotStatisitcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCommonProcessorSlotStatisitcs.setStatus("obsolete")
_CnCommonProcessorCCCardTypeStatisitcs_Type = CnCCCardType
_CnCommonProcessorCCCardTypeStatisitcs_Object = MibTableColumn
cnCommonProcessorCCCardTypeStatisitcs = _CnCommonProcessorCCCardTypeStatisitcs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 6, 1, 3),
    _CnCommonProcessorCCCardTypeStatisitcs_Type()
)
cnCommonProcessorCCCardTypeStatisitcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCommonProcessorCCCardTypeStatisitcs.setStatus("obsolete")
_CnCommonProcessorCardDiscoveredStatisitcs_Type = TruthValue
_CnCommonProcessorCardDiscoveredStatisitcs_Object = MibTableColumn
cnCommonProcessorCardDiscoveredStatisitcs = _CnCommonProcessorCardDiscoveredStatisitcs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 6, 1, 4),
    _CnCommonProcessorCardDiscoveredStatisitcs_Type()
)
cnCommonProcessorCardDiscoveredStatisitcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCommonProcessorCardDiscoveredStatisitcs.setStatus("obsolete")
_CnCommonProcessorCardStatusTypeStatisitics_Type = CnCardStatusType
_CnCommonProcessorCardStatusTypeStatisitics_Object = MibTableColumn
cnCommonProcessorCardStatusTypeStatisitics = _CnCommonProcessorCardStatusTypeStatisitics_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 6, 1, 5),
    _CnCommonProcessorCardStatusTypeStatisitics_Type()
)
cnCommonProcessorCardStatusTypeStatisitics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCommonProcessorCardStatusTypeStatisitics.setStatus("obsolete")


class _CnCommonProcessorMateSlotStatistics_Type(Integer32):
    """Custom type cnCommonProcessorMateSlotStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 47),
    )


_CnCommonProcessorMateSlotStatistics_Type.__name__ = "Integer32"
_CnCommonProcessorMateSlotStatistics_Object = MibTableColumn
cnCommonProcessorMateSlotStatistics = _CnCommonProcessorMateSlotStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 6, 1, 6),
    _CnCommonProcessorMateSlotStatistics_Type()
)
cnCommonProcessorMateSlotStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCommonProcessorMateSlotStatistics.setStatus("obsolete")
_CnCommonProcessorNumberOfLinksStatistics_Type = Integer32
_CnCommonProcessorNumberOfLinksStatistics_Object = MibTableColumn
cnCommonProcessorNumberOfLinksStatistics = _CnCommonProcessorNumberOfLinksStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 6, 1, 7),
    _CnCommonProcessorNumberOfLinksStatistics_Type()
)
cnCommonProcessorNumberOfLinksStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCommonProcessorNumberOfLinksStatistics.setStatus("obsolete")
_CnCommonProcessorLVDSLinkTypeStatistics_Type = Integer32
_CnCommonProcessorLVDSLinkTypeStatistics_Object = MibTableColumn
cnCommonProcessorLVDSLinkTypeStatistics = _CnCommonProcessorLVDSLinkTypeStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 6, 1, 8),
    _CnCommonProcessorLVDSLinkTypeStatistics_Type()
)
cnCommonProcessorLVDSLinkTypeStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCommonProcessorLVDSLinkTypeStatistics.setStatus("obsolete")
_CnCommonProcessorLVDSLinkCardTypeStatisitics_Type = CnCCCardType
_CnCommonProcessorLVDSLinkCardTypeStatisitics_Object = MibTableColumn
cnCommonProcessorLVDSLinkCardTypeStatisitics = _CnCommonProcessorLVDSLinkCardTypeStatisitics_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 6, 1, 9),
    _CnCommonProcessorLVDSLinkCardTypeStatisitics_Type()
)
cnCommonProcessorLVDSLinkCardTypeStatisitics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCommonProcessorLVDSLinkCardTypeStatisitics.setStatus("obsolete")
_CnCommonProcessorCpuStatisticsTable_Object = MibTable
cnCommonProcessorCpuStatisticsTable = _CnCommonProcessorCpuStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 7)
)
if mibBuilder.loadTexts:
    cnCommonProcessorCpuStatisticsTable.setStatus("current")
_CnCommonProcessorCpuStatisticsEntry_Object = MibTableRow
cnCommonProcessorCpuStatisticsEntry = _CnCommonProcessorCpuStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 7, 1)
)
cnCommonProcessorCpuStatisticsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cnCommonProcessorCpuStatisticsEntry.setStatus("current")
_CnCPCpuStatisticsShelf_Type = Unsigned32
_CnCPCpuStatisticsShelf_Object = MibTableColumn
cnCPCpuStatisticsShelf = _CnCPCpuStatisticsShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 7, 1, 1),
    _CnCPCpuStatisticsShelf_Type()
)
cnCPCpuStatisticsShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPCpuStatisticsShelf.setStatus("current")
_CnCPCpuStatisticsSlot_Type = Unsigned32
_CnCPCpuStatisticsSlot_Object = MibTableColumn
cnCPCpuStatisticsSlot = _CnCPCpuStatisticsSlot_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 7, 1, 2),
    _CnCPCpuStatisticsSlot_Type()
)
cnCPCpuStatisticsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPCpuStatisticsSlot.setStatus("current")
_CnCPCpuStatisticsCardType_Type = CnCCCardType
_CnCPCpuStatisticsCardType_Object = MibTableColumn
cnCPCpuStatisticsCardType = _CnCPCpuStatisticsCardType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 7, 1, 3),
    _CnCPCpuStatisticsCardType_Type()
)
cnCPCpuStatisticsCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPCpuStatisticsCardType.setStatus("current")
_CnCPCpuStatisticsAverageUtilization_Type = Integer32
_CnCPCpuStatisticsAverageUtilization_Object = MibTableColumn
cnCPCpuStatisticsAverageUtilization = _CnCPCpuStatisticsAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 7, 1, 4),
    _CnCPCpuStatisticsAverageUtilization_Type()
)
cnCPCpuStatisticsAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPCpuStatisticsAverageUtilization.setStatus("current")
_CnCPCpuStatisticsMaximumUtilization_Type = Integer32
_CnCPCpuStatisticsMaximumUtilization_Object = MibTableColumn
cnCPCpuStatisticsMaximumUtilization = _CnCPCpuStatisticsMaximumUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 7, 1, 5),
    _CnCPCpuStatisticsMaximumUtilization_Type()
)
cnCPCpuStatisticsMaximumUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPCpuStatisticsMaximumUtilization.setStatus("current")
_CnCPCpuStatisticsReset_Type = CnCPStatisticsReset
_CnCPCpuStatisticsReset_Object = MibTableColumn
cnCPCpuStatisticsReset = _CnCPCpuStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 7, 1, 6),
    _CnCPCpuStatisticsReset_Type()
)
cnCPCpuStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnCPCpuStatisticsReset.setStatus("current")
_CnCommonProcessorMessagingStatisticsTable_Object = MibTable
cnCommonProcessorMessagingStatisticsTable = _CnCommonProcessorMessagingStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 8)
)
if mibBuilder.loadTexts:
    cnCommonProcessorMessagingStatisticsTable.setStatus("current")
_CnCommonProcessorMessagingStatisticsEntry_Object = MibTableRow
cnCommonProcessorMessagingStatisticsEntry = _CnCommonProcessorMessagingStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 8, 1)
)
cnCommonProcessorMessagingStatisticsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cnCommonProcessorMessagingStatisticsEntry.setStatus("current")
_CnCPMessagingStatisticsShelf_Type = Unsigned32
_CnCPMessagingStatisticsShelf_Object = MibTableColumn
cnCPMessagingStatisticsShelf = _CnCPMessagingStatisticsShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 8, 1, 1),
    _CnCPMessagingStatisticsShelf_Type()
)
cnCPMessagingStatisticsShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMessagingStatisticsShelf.setStatus("current")
_CnCPMessagingStatisticsSlot_Type = Unsigned32
_CnCPMessagingStatisticsSlot_Object = MibTableColumn
cnCPMessagingStatisticsSlot = _CnCPMessagingStatisticsSlot_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 8, 1, 2),
    _CnCPMessagingStatisticsSlot_Type()
)
cnCPMessagingStatisticsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMessagingStatisticsSlot.setStatus("current")
_CnCPMessagingStatisticsCardType_Type = CnCCCardType
_CnCPMessagingStatisticsCardType_Object = MibTableColumn
cnCPMessagingStatisticsCardType = _CnCPMessagingStatisticsCardType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 8, 1, 3),
    _CnCPMessagingStatisticsCardType_Type()
)
cnCPMessagingStatisticsCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMessagingStatisticsCardType.setStatus("current")
_CnCPMessagingStatisticsAverageUtilization_Type = Integer32
_CnCPMessagingStatisticsAverageUtilization_Object = MibTableColumn
cnCPMessagingStatisticsAverageUtilization = _CnCPMessagingStatisticsAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 8, 1, 4),
    _CnCPMessagingStatisticsAverageUtilization_Type()
)
cnCPMessagingStatisticsAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMessagingStatisticsAverageUtilization.setStatus("current")
_CnCPMessagingStatisticsMaximumUtilization_Type = Integer32
_CnCPMessagingStatisticsMaximumUtilization_Object = MibTableColumn
cnCPMessagingStatisticsMaximumUtilization = _CnCPMessagingStatisticsMaximumUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 8, 1, 5),
    _CnCPMessagingStatisticsMaximumUtilization_Type()
)
cnCPMessagingStatisticsMaximumUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMessagingStatisticsMaximumUtilization.setStatus("current")
_CnCPMessagingStatisticsReset_Type = CnCPStatisticsReset
_CnCPMessagingStatisticsReset_Object = MibTableColumn
cnCPMessagingStatisticsReset = _CnCPMessagingStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 8, 1, 6),
    _CnCPMessagingStatisticsReset_Type()
)
cnCPMessagingStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnCPMessagingStatisticsReset.setStatus("current")
_CnCommonProcessorMemoryStatisticsTable_Object = MibTable
cnCommonProcessorMemoryStatisticsTable = _CnCommonProcessorMemoryStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 9)
)
if mibBuilder.loadTexts:
    cnCommonProcessorMemoryStatisticsTable.setStatus("current")
_CnCommonProcessorMemoryStatisticsEntry_Object = MibTableRow
cnCommonProcessorMemoryStatisticsEntry = _CnCommonProcessorMemoryStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 9, 1)
)
cnCommonProcessorMemoryStatisticsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cnCommonProcessorMemoryStatisticsEntry.setStatus("current")
_CnCPMemoryStatisticsShelf_Type = Unsigned32
_CnCPMemoryStatisticsShelf_Object = MibTableColumn
cnCPMemoryStatisticsShelf = _CnCPMemoryStatisticsShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 9, 1, 1),
    _CnCPMemoryStatisticsShelf_Type()
)
cnCPMemoryStatisticsShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMemoryStatisticsShelf.setStatus("current")
_CnCPMemoryStatisticsSlot_Type = Unsigned32
_CnCPMemoryStatisticsSlot_Object = MibTableColumn
cnCPMemoryStatisticsSlot = _CnCPMemoryStatisticsSlot_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 9, 1, 2),
    _CnCPMemoryStatisticsSlot_Type()
)
cnCPMemoryStatisticsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMemoryStatisticsSlot.setStatus("current")
_CnCPMemoryStatisticsCardType_Type = CnCCCardType
_CnCPMemoryStatisticsCardType_Object = MibTableColumn
cnCPMemoryStatisticsCardType = _CnCPMemoryStatisticsCardType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 9, 1, 3),
    _CnCPMemoryStatisticsCardType_Type()
)
cnCPMemoryStatisticsCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMemoryStatisticsCardType.setStatus("current")
_CnCPMemoryStatisticsAverageUtilization_Type = Integer32
_CnCPMemoryStatisticsAverageUtilization_Object = MibTableColumn
cnCPMemoryStatisticsAverageUtilization = _CnCPMemoryStatisticsAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 9, 1, 4),
    _CnCPMemoryStatisticsAverageUtilization_Type()
)
cnCPMemoryStatisticsAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMemoryStatisticsAverageUtilization.setStatus("current")
_CnCPMemoryStatisticsMaximumUtilization_Type = Integer32
_CnCPMemoryStatisticsMaximumUtilization_Object = MibTableColumn
cnCPMemoryStatisticsMaximumUtilization = _CnCPMemoryStatisticsMaximumUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 9, 1, 5),
    _CnCPMemoryStatisticsMaximumUtilization_Type()
)
cnCPMemoryStatisticsMaximumUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMemoryStatisticsMaximumUtilization.setStatus("current")
_CnCPMemoryStatisticsReset_Type = CnCPStatisticsReset
_CnCPMemoryStatisticsReset_Object = MibTableColumn
cnCPMemoryStatisticsReset = _CnCPMemoryStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 9, 1, 6),
    _CnCPMemoryStatisticsReset_Type()
)
cnCPMemoryStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnCPMemoryStatisticsReset.setStatus("current")
_CnCommonProcessorBandwidthStatisticsTable_Object = MibTable
cnCommonProcessorBandwidthStatisticsTable = _CnCommonProcessorBandwidthStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 10)
)
if mibBuilder.loadTexts:
    cnCommonProcessorBandwidthStatisticsTable.setStatus("current")
_CnCommonProcessorBandwidthStatisticsEntry_Object = MibTableRow
cnCommonProcessorBandwidthStatisticsEntry = _CnCommonProcessorBandwidthStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 10, 1)
)
cnCommonProcessorBandwidthStatisticsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cnCommonProcessorBandwidthStatisticsEntry.setStatus("current")
_CnCPBandwidthStatisticsShelf_Type = Unsigned32
_CnCPBandwidthStatisticsShelf_Object = MibTableColumn
cnCPBandwidthStatisticsShelf = _CnCPBandwidthStatisticsShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 10, 1, 1),
    _CnCPBandwidthStatisticsShelf_Type()
)
cnCPBandwidthStatisticsShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPBandwidthStatisticsShelf.setStatus("current")
_CnCPBandwidthStatisticsSlot_Type = Unsigned32
_CnCPBandwidthStatisticsSlot_Object = MibTableColumn
cnCPBandwidthStatisticsSlot = _CnCPBandwidthStatisticsSlot_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 10, 1, 2),
    _CnCPBandwidthStatisticsSlot_Type()
)
cnCPBandwidthStatisticsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPBandwidthStatisticsSlot.setStatus("current")
_CnCPBandwidthStatisticsCardType_Type = CnCCCardType
_CnCPBandwidthStatisticsCardType_Object = MibTableColumn
cnCPBandwidthStatisticsCardType = _CnCPBandwidthStatisticsCardType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 10, 1, 3),
    _CnCPBandwidthStatisticsCardType_Type()
)
cnCPBandwidthStatisticsCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPBandwidthStatisticsCardType.setStatus("current")
_CnCPBandwidthStatisticsSystemUtilization_Type = Integer32
_CnCPBandwidthStatisticsSystemUtilization_Object = MibTableColumn
cnCPBandwidthStatisticsSystemUtilization = _CnCPBandwidthStatisticsSystemUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 10, 1, 4),
    _CnCPBandwidthStatisticsSystemUtilization_Type()
)
cnCPBandwidthStatisticsSystemUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPBandwidthStatisticsSystemUtilization.setStatus("current")
_CnCPBandwidthStatisticsCbrVbrBufferUtilization_Type = Integer32
_CnCPBandwidthStatisticsCbrVbrBufferUtilization_Object = MibTableColumn
cnCPBandwidthStatisticsCbrVbrBufferUtilization = _CnCPBandwidthStatisticsCbrVbrBufferUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 10, 1, 5),
    _CnCPBandwidthStatisticsCbrVbrBufferUtilization_Type()
)
cnCPBandwidthStatisticsCbrVbrBufferUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPBandwidthStatisticsCbrVbrBufferUtilization.setStatus("current")
_CnCPBandwidthStatisticsAdslUtilization_Type = Integer32
_CnCPBandwidthStatisticsAdslUtilization_Object = MibTableColumn
cnCPBandwidthStatisticsAdslUtilization = _CnCPBandwidthStatisticsAdslUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 10, 1, 6),
    _CnCPBandwidthStatisticsAdslUtilization_Type()
)
cnCPBandwidthStatisticsAdslUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPBandwidthStatisticsAdslUtilization.setStatus("current")
_CnCPBandwidthStatisticsReset_Type = CnCPStatisticsReset
_CnCPBandwidthStatisticsReset_Object = MibTableColumn
cnCPBandwidthStatisticsReset = _CnCPBandwidthStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 10, 1, 7),
    _CnCPBandwidthStatisticsReset_Type()
)
cnCPBandwidthStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnCPBandwidthStatisticsReset.setStatus("current")
_CnCommonProcessorMessagePoolStatisticsTable_Object = MibTable
cnCommonProcessorMessagePoolStatisticsTable = _CnCommonProcessorMessagePoolStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 11)
)
if mibBuilder.loadTexts:
    cnCommonProcessorMessagePoolStatisticsTable.setStatus("current")
_CnCommonProcessorMessagePoolStatisticsEntry_Object = MibTableRow
cnCommonProcessorMessagePoolStatisticsEntry = _CnCommonProcessorMessagePoolStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 11, 1)
)
cnCommonProcessorMessagePoolStatisticsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CEM-COMMON-PROCESSOR", "cnCPMessagePoolNumber"),
)
if mibBuilder.loadTexts:
    cnCommonProcessorMessagePoolStatisticsEntry.setStatus("current")
_CnCPMessagePoolStatisticsShelf_Type = Unsigned32
_CnCPMessagePoolStatisticsShelf_Object = MibTableColumn
cnCPMessagePoolStatisticsShelf = _CnCPMessagePoolStatisticsShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 11, 1, 1),
    _CnCPMessagePoolStatisticsShelf_Type()
)
cnCPMessagePoolStatisticsShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMessagePoolStatisticsShelf.setStatus("current")
_CnCPMessagePoolStatisticsSlot_Type = Unsigned32
_CnCPMessagePoolStatisticsSlot_Object = MibTableColumn
cnCPMessagePoolStatisticsSlot = _CnCPMessagePoolStatisticsSlot_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 11, 1, 2),
    _CnCPMessagePoolStatisticsSlot_Type()
)
cnCPMessagePoolStatisticsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMessagePoolStatisticsSlot.setStatus("current")
_CnCPMessagePoolStatisticsCardType_Type = CnCCCardType
_CnCPMessagePoolStatisticsCardType_Object = MibTableColumn
cnCPMessagePoolStatisticsCardType = _CnCPMessagePoolStatisticsCardType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 11, 1, 3),
    _CnCPMessagePoolStatisticsCardType_Type()
)
cnCPMessagePoolStatisticsCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMessagePoolStatisticsCardType.setStatus("current")


class _CnCPMessagePoolNumber_Type(Integer32):
    """Custom type cnCPMessagePoolNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CnCPMessagePoolNumber_Type.__name__ = "Integer32"
_CnCPMessagePoolNumber_Object = MibTableColumn
cnCPMessagePoolNumber = _CnCPMessagePoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 11, 1, 4),
    _CnCPMessagePoolNumber_Type()
)
cnCPMessagePoolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMessagePoolNumber.setStatus("current")
_CnCPMessagePoolAverageUtilization_Type = Integer32
_CnCPMessagePoolAverageUtilization_Object = MibTableColumn
cnCPMessagePoolAverageUtilization = _CnCPMessagePoolAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 11, 1, 5),
    _CnCPMessagePoolAverageUtilization_Type()
)
cnCPMessagePoolAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMessagePoolAverageUtilization.setStatus("current")
_CnCPMessagePoolMaximumUtilization_Type = Integer32
_CnCPMessagePoolMaximumUtilization_Object = MibTableColumn
cnCPMessagePoolMaximumUtilization = _CnCPMessagePoolMaximumUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 11, 1, 6),
    _CnCPMessagePoolMaximumUtilization_Type()
)
cnCPMessagePoolMaximumUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMessagePoolMaximumUtilization.setStatus("current")
_CnCPMessagePoolReset_Type = CnCPStatisticsReset
_CnCPMessagePoolReset_Object = MibTableColumn
cnCPMessagePoolReset = _CnCPMessagePoolReset_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 11, 1, 7),
    _CnCPMessagePoolReset_Type()
)
cnCPMessagePoolReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnCPMessagePoolReset.setStatus("current")
_CnCommonProcessorMemoryPoolStatisticsTable_Object = MibTable
cnCommonProcessorMemoryPoolStatisticsTable = _CnCommonProcessorMemoryPoolStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 12)
)
if mibBuilder.loadTexts:
    cnCommonProcessorMemoryPoolStatisticsTable.setStatus("current")
_CnCommonProcessorMemoryPoolStatisticsEntry_Object = MibTableRow
cnCommonProcessorMemoryPoolStatisticsEntry = _CnCommonProcessorMemoryPoolStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 12, 1)
)
cnCommonProcessorMemoryPoolStatisticsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CEM-COMMON-PROCESSOR", "cnCPMemoryPoolNumber"),
)
if mibBuilder.loadTexts:
    cnCommonProcessorMemoryPoolStatisticsEntry.setStatus("current")
_CnCPMemoryPoolStatisticsShelf_Type = Unsigned32
_CnCPMemoryPoolStatisticsShelf_Object = MibTableColumn
cnCPMemoryPoolStatisticsShelf = _CnCPMemoryPoolStatisticsShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 12, 1, 1),
    _CnCPMemoryPoolStatisticsShelf_Type()
)
cnCPMemoryPoolStatisticsShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMemoryPoolStatisticsShelf.setStatus("current")
_CnCPMemoryPoolStatisticsSlot_Type = Unsigned32
_CnCPMemoryPoolStatisticsSlot_Object = MibTableColumn
cnCPMemoryPoolStatisticsSlot = _CnCPMemoryPoolStatisticsSlot_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 12, 1, 2),
    _CnCPMemoryPoolStatisticsSlot_Type()
)
cnCPMemoryPoolStatisticsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMemoryPoolStatisticsSlot.setStatus("current")
_CnCPMemoryPoolStatisticsCardType_Type = CnCCCardType
_CnCPMemoryPoolStatisticsCardType_Object = MibTableColumn
cnCPMemoryPoolStatisticsCardType = _CnCPMemoryPoolStatisticsCardType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 12, 1, 3),
    _CnCPMemoryPoolStatisticsCardType_Type()
)
cnCPMemoryPoolStatisticsCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMemoryPoolStatisticsCardType.setStatus("current")


class _CnCPMemoryPoolNumber_Type(Integer32):
    """Custom type cnCPMemoryPoolNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CnCPMemoryPoolNumber_Type.__name__ = "Integer32"
_CnCPMemoryPoolNumber_Object = MibTableColumn
cnCPMemoryPoolNumber = _CnCPMemoryPoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 12, 1, 4),
    _CnCPMemoryPoolNumber_Type()
)
cnCPMemoryPoolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMemoryPoolNumber.setStatus("current")
_CnCPMemoryPoolAverageUtilization_Type = Integer32
_CnCPMemoryPoolAverageUtilization_Object = MibTableColumn
cnCPMemoryPoolAverageUtilization = _CnCPMemoryPoolAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 12, 1, 5),
    _CnCPMemoryPoolAverageUtilization_Type()
)
cnCPMemoryPoolAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMemoryPoolAverageUtilization.setStatus("current")
_CnCPMemoryPoolMaximumUtilization_Type = Integer32
_CnCPMemoryPoolMaximumUtilization_Object = MibTableColumn
cnCPMemoryPoolMaximumUtilization = _CnCPMemoryPoolMaximumUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 12, 1, 6),
    _CnCPMemoryPoolMaximumUtilization_Type()
)
cnCPMemoryPoolMaximumUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnCPMemoryPoolMaximumUtilization.setStatus("current")
_CnCPMemoryPoolReset_Type = CnCPStatisticsReset
_CnCPMemoryPoolReset_Object = MibTableColumn
cnCPMemoryPoolReset = _CnCPMemoryPoolReset_Object(
    (1, 3, 6, 1, 4, 1, 6352, 7, 12, 1, 7),
    _CnCPMemoryPoolReset_Type()
)
cnCPMemoryPoolReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnCPMemoryPoolReset.setStatus("current")
_CnCommonProcessorNotifications_ObjectIdentity = ObjectIdentity
cnCommonProcessorNotifications = _CnCommonProcessorNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 7, 13)
)
_CnCommonProcessorGroups_ObjectIdentity = ObjectIdentity
cnCommonProcessorGroups = _CnCommonProcessorGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 7, 14)
)

# Managed Objects groups

cnCommonProcessorCN1000ObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 7, 14, 1)
)
cnCommonProcessorCN1000ObjectGroup.setObjects(
      *(("CEM-COMMON-PROCESSOR", "cnCPFirmwareImageName"),
        ("CEM-COMMON-PROCESSOR", "cnCPFirmwareSize"),
        ("CEM-COMMON-PROCESSOR", "cnCPFirmwareBuildDate"),
        ("CEM-COMMON-PROCESSOR", "cnCPBankAImageName"),
        ("CEM-COMMON-PROCESSOR", "cnCPBankABuildDate"),
        ("CEM-COMMON-PROCESSOR", "cnCPBankADateWritten"),
        ("CEM-COMMON-PROCESSOR", "cnCPBankBImageName"),
        ("CEM-COMMON-PROCESSOR", "cnCPBankBBuildDate"),
        ("CEM-COMMON-PROCESSOR", "cnCPBankBDateWritten"),
        ("CEM-COMMON-PROCESSOR", "cnCPNextBootBank"),
        ("CEM-COMMON-PROCESSOR", "cnCPActiveBootBank"),
        ("CEM-COMMON-PROCESSOR", "cnCPActiveBankControl"),
        ("CEM-COMMON-PROCESSOR", "cnCPBootBankCardType"),
        ("CEM-COMMON-PROCESSOR", "cnCPBootBankShelfNumber"),
        ("CEM-COMMON-PROCESSOR", "cnCPBootBankSlotNumber"),
        ("CEM-COMMON-PROCESSOR", "cnCPFirmwareDateWritten"),
        ("CEM-COMMON-PROCESSOR", "cnCPBankASize"),
        ("CEM-COMMON-PROCESSOR", "cnCPBankBSize"),
        ("CEM-COMMON-PROCESSOR", "cnCPCpuStatisticsReset"),
        ("CEM-COMMON-PROCESSOR", "cnCPCpuStatisticsMaximumUtilization"),
        ("CEM-COMMON-PROCESSOR", "cnCPCpuStatisticsCardType"),
        ("CEM-COMMON-PROCESSOR", "cnCPCpuStatisticsSlot"),
        ("CEM-COMMON-PROCESSOR", "cnCPCpuStatisticsShelf"),
        ("CEM-COMMON-PROCESSOR", "cnCPMessagingStatisticsShelf"),
        ("CEM-COMMON-PROCESSOR", "cnCPMessagingStatisticsSlot"),
        ("CEM-COMMON-PROCESSOR", "cnCPMessagingStatisticsCardType"),
        ("CEM-COMMON-PROCESSOR", "cnCPMessagingStatisticsAverageUtilization"),
        ("CEM-COMMON-PROCESSOR", "cnCPMessagingStatisticsMaximumUtilization"),
        ("CEM-COMMON-PROCESSOR", "cnCPMessagingStatisticsReset"),
        ("CEM-COMMON-PROCESSOR", "cnCPMemoryStatisticsShelf"),
        ("CEM-COMMON-PROCESSOR", "cnCPMemoryStatisticsSlot"),
        ("CEM-COMMON-PROCESSOR", "cnCPMemoryStatisticsCardType"),
        ("CEM-COMMON-PROCESSOR", "cnCPMemoryStatisticsAverageUtilization"),
        ("CEM-COMMON-PROCESSOR", "cnCPMemoryStatisticsMaximumUtilization"),
        ("CEM-COMMON-PROCESSOR", "cnCPMemoryStatisticsReset"),
        ("CEM-COMMON-PROCESSOR", "cnCPBandwidthStatisticsShelf"),
        ("CEM-COMMON-PROCESSOR", "cnCPBandwidthStatisticsSlot"),
        ("CEM-COMMON-PROCESSOR", "cnCPBandwidthStatisticsCardType"),
        ("CEM-COMMON-PROCESSOR", "cnCPBandwidthStatisticsSystemUtilization"),
        ("CEM-COMMON-PROCESSOR", "cnCPBandwidthStatisticsCbrVbrBufferUtilization"),
        ("CEM-COMMON-PROCESSOR", "cnCPBandwidthStatisticsAdslUtilization"),
        ("CEM-COMMON-PROCESSOR", "cnCPBandwidthStatisticsReset"),
        ("CEM-COMMON-PROCESSOR", "cnCPMessagePoolStatisticsShelf"),
        ("CEM-COMMON-PROCESSOR", "cnCPMessagePoolStatisticsSlot"),
        ("CEM-COMMON-PROCESSOR", "cnCPMessagePoolNumber"),
        ("CEM-COMMON-PROCESSOR", "cnCPMessagePoolAverageUtilization"),
        ("CEM-COMMON-PROCESSOR", "cnCPMessagePoolMaximumUtilization"),
        ("CEM-COMMON-PROCESSOR", "cnCPMemoryPoolStatisticsShelf"),
        ("CEM-COMMON-PROCESSOR", "cnCPMemoryPoolStatisticsSlot"),
        ("CEM-COMMON-PROCESSOR", "cnCPMemoryPoolStatisticsCardType"),
        ("CEM-COMMON-PROCESSOR", "cnCPMessagePoolStatisticsCardType"),
        ("CEM-COMMON-PROCESSOR", "cnCPMemoryPoolAverageUtilization"),
        ("CEM-COMMON-PROCESSOR", "cnCPMessagePoolReset"),
        ("CEM-COMMON-PROCESSOR", "cnCPMemoryPoolReset"),
        ("CEM-COMMON-PROCESSOR", "cnCPMemoryPoolMaximumUtilization"),
        ("CEM-COMMON-PROCESSOR", "cnCPCpuStatisticsAverageUtilization"),
        ("CEM-COMMON-PROCESSOR", "cnCPMemoryPoolNumber"))
)
if mibBuilder.loadTexts:
    cnCommonProcessorCN1000ObjectGroup.setStatus("current")

cnCommonProcessorObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 7, 14, 4)
)
cnCommonProcessorObsoleteGroup.setObjects(
      *(("CEM-COMMON-PROCESSOR", "cnCPProcessorType"),
        ("CEM-COMMON-PROCESSOR", "cnCPProcessorAndSpeedInMHz"),
        ("CEM-COMMON-PROCESSOR", "cnCPRAMinMBytes"),
        ("CEM-COMMON-PROCESSOR", "cnCPProcessorUtilization"),
        ("CEM-COMMON-PROCESSOR", "cnCPCurrentProcessorFreeMemory"),
        ("CEM-COMMON-PROCESSOR", "cnCPCurrentProcessorLargestAvailableMemoryFragment"),
        ("CEM-COMMON-PROCESSOR", "cnCPShelfNumber"),
        ("CEM-COMMON-PROCESSOR", "cnCPSlotNumber"),
        ("CEM-COMMON-PROCESSOR", "cnCPCardType"),
        ("CEM-COMMON-PROCESSOR", "cnCPIntervalProcessorStatisticsType"),
        ("CEM-COMMON-PROCESSOR", "cnCPProcessorStatisticsIntervalIndex"),
        ("CEM-COMMON-PROCESSOR", "cnCPIntervalProcessorFreeMemory"),
        ("CEM-COMMON-PROCESSOR", "cnCPIntervalProcessorLargestAvailableMemoryFragment"),
        ("CEM-COMMON-PROCESSOR", "cnCPCardTypeStatistics"),
        ("CEM-COMMON-PROCESSOR", "cnCommonProcessorShelfStatisitcs"),
        ("CEM-COMMON-PROCESSOR", "cnCommonProcessorSlotStatisitcs"),
        ("CEM-COMMON-PROCESSOR", "cnCommonProcessorCCCardTypeStatisitcs"),
        ("CEM-COMMON-PROCESSOR", "cnCommonProcessorCardDiscoveredStatisitcs"),
        ("CEM-COMMON-PROCESSOR", "cnCommonProcessorCardStatusTypeStatisitics"),
        ("CEM-COMMON-PROCESSOR", "cnCommonProcessorMateSlotStatistics"),
        ("CEM-COMMON-PROCESSOR", "cnCommonProcessorNumberOfLinksStatistics"),
        ("CEM-COMMON-PROCESSOR", "cnCommonProcessorLVDSLinkTypeStatistics"),
        ("CEM-COMMON-PROCESSOR", "cnCommonProcessorLVDSLinkCardTypeStatisitics"))
)
if mibBuilder.loadTexts:
    cnCommonProcessorObsoleteGroup.setStatus("obsolete")


# Notification objects

cnCPUnknownLoadInActiveBank = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 7, 13, 1)
)
cnCPUnknownLoadInActiveBank.setObjects(
      *(("CEM-COMMON-PROCESSOR", "cnCPActiveBootBank"),
        ("CEM-COMMON-PROCESSOR", "cnCPBankAImageName"),
        ("CEM-COMMON-PROCESSOR", "cnCPBankBImageName"))
)
if mibBuilder.loadTexts:
    cnCPUnknownLoadInActiveBank.setStatus(
        "current"
    )

cnCPUpgradeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 7, 13, 2)
)
cnCPUpgradeFailed.setObjects(
      *(("CEM-COMMON-PROCESSOR", "cnCPActiveBootBank"),
        ("CEM-COMMON-PROCESSOR", "cnCPBankAImageName"),
        ("CEM-COMMON-PROCESSOR", "cnCPBankBImageName"))
)
if mibBuilder.loadTexts:
    cnCPUpgradeFailed.setStatus(
        "current"
    )


# Notifications groups

cnCommonProcessorNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6352, 7, 14, 3)
)
cnCommonProcessorNotificationGroup.setObjects(
      *(("CEM-COMMON-PROCESSOR", "cnCPUnknownLoadInActiveBank"),
        ("CEM-COMMON-PROCESSOR", "cnCPUpgradeFailed"))
)
if mibBuilder.loadTexts:
    cnCommonProcessorNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cnCommonProcessorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6352, 7, 14, 2)
)
cnCommonProcessorCompliance.setObjects(
      *(("CEM-COMMON-PROCESSOR", "cnCommonProcessorNotificationGroup"),
        ("CEM-COMMON-PROCESSOR", "cnCommonProcessorCN1000ObjectGroup"))
)
if mibBuilder.loadTexts:
    cnCommonProcessorCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-COMMON-PROCESSOR",
    **{"CnCPProcessorType": CnCPProcessorType,
       "CnCCCardType": CnCCCardType,
       "CnCPBanks": CnCPBanks,
       "CnCPActiveBankControlType": CnCPActiveBankControlType,
       "CnCPProcessorStatisticsType": CnCPProcessorStatisticsType,
       "CnCardStatusType": CnCardStatusType,
       "CnCPStatisticsReset": CnCPStatisticsReset,
       "cnCommonProcessorModule": cnCommonProcessorModule,
       "cnCommonProcessorTable": cnCommonProcessorTable,
       "cnCommonProcessorEntry": cnCommonProcessorEntry,
       "cnCPProcessorType": cnCPProcessorType,
       "cnCPProcessorAndSpeedInMHz": cnCPProcessorAndSpeedInMHz,
       "cnCPRAMinMBytes": cnCPRAMinMBytes,
       "cnCPProcessorUtilization": cnCPProcessorUtilization,
       "cnCPCurrentProcessorFreeMemory": cnCPCurrentProcessorFreeMemory,
       "cnCPCurrentProcessorLargestAvailableMemoryFragment": cnCPCurrentProcessorLargestAvailableMemoryFragment,
       "cnCPShelfNumber": cnCPShelfNumber,
       "cnCPSlotNumber": cnCPSlotNumber,
       "cnCPCardType": cnCPCardType,
       "cnCommonProcessorBootBankTable": cnCommonProcessorBootBankTable,
       "cnCommonProcessorBootBankEntry": cnCommonProcessorBootBankEntry,
       "cnCPFirmwareImageName": cnCPFirmwareImageName,
       "cnCPFirmwareSize": cnCPFirmwareSize,
       "cnCPFirmwareBuildDate": cnCPFirmwareBuildDate,
       "cnCPFirmwareDateWritten": cnCPFirmwareDateWritten,
       "cnCPBankAImageName": cnCPBankAImageName,
       "cnCPBankASize": cnCPBankASize,
       "cnCPBankABuildDate": cnCPBankABuildDate,
       "cnCPBankADateWritten": cnCPBankADateWritten,
       "cnCPBankBImageName": cnCPBankBImageName,
       "cnCPBankBSize": cnCPBankBSize,
       "cnCPBankBBuildDate": cnCPBankBBuildDate,
       "cnCPBankBDateWritten": cnCPBankBDateWritten,
       "cnCPNextBootBank": cnCPNextBootBank,
       "cnCPActiveBootBank": cnCPActiveBootBank,
       "cnCPActiveBankControl": cnCPActiveBankControl,
       "cnCPBootBankCardType": cnCPBootBankCardType,
       "cnCPBootBankShelfNumber": cnCPBootBankShelfNumber,
       "cnCPBootBankSlotNumber": cnCPBootBankSlotNumber,
       "cnCommonProcessorStatisticsTable": cnCommonProcessorStatisticsTable,
       "cnCommonProcessorStatisticsEntry": cnCommonProcessorStatisticsEntry,
       "cnCPIntervalProcessorStatisticsType": cnCPIntervalProcessorStatisticsType,
       "cnCPProcessorStatisticsIntervalIndex": cnCPProcessorStatisticsIntervalIndex,
       "cnCPIntervalProcessorFreeMemory": cnCPIntervalProcessorFreeMemory,
       "cnCPIntervalProcessorLargestAvailableMemoryFragment": cnCPIntervalProcessorLargestAvailableMemoryFragment,
       "cnCPCardTypeStatistics": cnCPCardTypeStatistics,
       "cnCommonProcessorLVDSStatisticsTable": cnCommonProcessorLVDSStatisticsTable,
       "cnCommonProcessorLVDSStatisticsEntry": cnCommonProcessorLVDSStatisticsEntry,
       "cnCommonProcessorShelfStatisitcs": cnCommonProcessorShelfStatisitcs,
       "cnCommonProcessorSlotStatisitcs": cnCommonProcessorSlotStatisitcs,
       "cnCommonProcessorCCCardTypeStatisitcs": cnCommonProcessorCCCardTypeStatisitcs,
       "cnCommonProcessorCardDiscoveredStatisitcs": cnCommonProcessorCardDiscoveredStatisitcs,
       "cnCommonProcessorCardStatusTypeStatisitics": cnCommonProcessorCardStatusTypeStatisitics,
       "cnCommonProcessorMateSlotStatistics": cnCommonProcessorMateSlotStatistics,
       "cnCommonProcessorNumberOfLinksStatistics": cnCommonProcessorNumberOfLinksStatistics,
       "cnCommonProcessorLVDSLinkTypeStatistics": cnCommonProcessorLVDSLinkTypeStatistics,
       "cnCommonProcessorLVDSLinkCardTypeStatisitics": cnCommonProcessorLVDSLinkCardTypeStatisitics,
       "cnCommonProcessorCpuStatisticsTable": cnCommonProcessorCpuStatisticsTable,
       "cnCommonProcessorCpuStatisticsEntry": cnCommonProcessorCpuStatisticsEntry,
       "cnCPCpuStatisticsShelf": cnCPCpuStatisticsShelf,
       "cnCPCpuStatisticsSlot": cnCPCpuStatisticsSlot,
       "cnCPCpuStatisticsCardType": cnCPCpuStatisticsCardType,
       "cnCPCpuStatisticsAverageUtilization": cnCPCpuStatisticsAverageUtilization,
       "cnCPCpuStatisticsMaximumUtilization": cnCPCpuStatisticsMaximumUtilization,
       "cnCPCpuStatisticsReset": cnCPCpuStatisticsReset,
       "cnCommonProcessorMessagingStatisticsTable": cnCommonProcessorMessagingStatisticsTable,
       "cnCommonProcessorMessagingStatisticsEntry": cnCommonProcessorMessagingStatisticsEntry,
       "cnCPMessagingStatisticsShelf": cnCPMessagingStatisticsShelf,
       "cnCPMessagingStatisticsSlot": cnCPMessagingStatisticsSlot,
       "cnCPMessagingStatisticsCardType": cnCPMessagingStatisticsCardType,
       "cnCPMessagingStatisticsAverageUtilization": cnCPMessagingStatisticsAverageUtilization,
       "cnCPMessagingStatisticsMaximumUtilization": cnCPMessagingStatisticsMaximumUtilization,
       "cnCPMessagingStatisticsReset": cnCPMessagingStatisticsReset,
       "cnCommonProcessorMemoryStatisticsTable": cnCommonProcessorMemoryStatisticsTable,
       "cnCommonProcessorMemoryStatisticsEntry": cnCommonProcessorMemoryStatisticsEntry,
       "cnCPMemoryStatisticsShelf": cnCPMemoryStatisticsShelf,
       "cnCPMemoryStatisticsSlot": cnCPMemoryStatisticsSlot,
       "cnCPMemoryStatisticsCardType": cnCPMemoryStatisticsCardType,
       "cnCPMemoryStatisticsAverageUtilization": cnCPMemoryStatisticsAverageUtilization,
       "cnCPMemoryStatisticsMaximumUtilization": cnCPMemoryStatisticsMaximumUtilization,
       "cnCPMemoryStatisticsReset": cnCPMemoryStatisticsReset,
       "cnCommonProcessorBandwidthStatisticsTable": cnCommonProcessorBandwidthStatisticsTable,
       "cnCommonProcessorBandwidthStatisticsEntry": cnCommonProcessorBandwidthStatisticsEntry,
       "cnCPBandwidthStatisticsShelf": cnCPBandwidthStatisticsShelf,
       "cnCPBandwidthStatisticsSlot": cnCPBandwidthStatisticsSlot,
       "cnCPBandwidthStatisticsCardType": cnCPBandwidthStatisticsCardType,
       "cnCPBandwidthStatisticsSystemUtilization": cnCPBandwidthStatisticsSystemUtilization,
       "cnCPBandwidthStatisticsCbrVbrBufferUtilization": cnCPBandwidthStatisticsCbrVbrBufferUtilization,
       "cnCPBandwidthStatisticsAdslUtilization": cnCPBandwidthStatisticsAdslUtilization,
       "cnCPBandwidthStatisticsReset": cnCPBandwidthStatisticsReset,
       "cnCommonProcessorMessagePoolStatisticsTable": cnCommonProcessorMessagePoolStatisticsTable,
       "cnCommonProcessorMessagePoolStatisticsEntry": cnCommonProcessorMessagePoolStatisticsEntry,
       "cnCPMessagePoolStatisticsShelf": cnCPMessagePoolStatisticsShelf,
       "cnCPMessagePoolStatisticsSlot": cnCPMessagePoolStatisticsSlot,
       "cnCPMessagePoolStatisticsCardType": cnCPMessagePoolStatisticsCardType,
       "cnCPMessagePoolNumber": cnCPMessagePoolNumber,
       "cnCPMessagePoolAverageUtilization": cnCPMessagePoolAverageUtilization,
       "cnCPMessagePoolMaximumUtilization": cnCPMessagePoolMaximumUtilization,
       "cnCPMessagePoolReset": cnCPMessagePoolReset,
       "cnCommonProcessorMemoryPoolStatisticsTable": cnCommonProcessorMemoryPoolStatisticsTable,
       "cnCommonProcessorMemoryPoolStatisticsEntry": cnCommonProcessorMemoryPoolStatisticsEntry,
       "cnCPMemoryPoolStatisticsShelf": cnCPMemoryPoolStatisticsShelf,
       "cnCPMemoryPoolStatisticsSlot": cnCPMemoryPoolStatisticsSlot,
       "cnCPMemoryPoolStatisticsCardType": cnCPMemoryPoolStatisticsCardType,
       "cnCPMemoryPoolNumber": cnCPMemoryPoolNumber,
       "cnCPMemoryPoolAverageUtilization": cnCPMemoryPoolAverageUtilization,
       "cnCPMemoryPoolMaximumUtilization": cnCPMemoryPoolMaximumUtilization,
       "cnCPMemoryPoolReset": cnCPMemoryPoolReset,
       "cnCommonProcessorNotifications": cnCommonProcessorNotifications,
       "cnCPUnknownLoadInActiveBank": cnCPUnknownLoadInActiveBank,
       "cnCPUpgradeFailed": cnCPUpgradeFailed,
       "cnCommonProcessorGroups": cnCommonProcessorGroups,
       "cnCommonProcessorCN1000ObjectGroup": cnCommonProcessorCN1000ObjectGroup,
       "cnCommonProcessorCompliance": cnCommonProcessorCompliance,
       "cnCommonProcessorNotificationGroup": cnCommonProcessorNotificationGroup,
       "cnCommonProcessorObsoleteGroup": cnCommonProcessorObsoleteGroup}
)
