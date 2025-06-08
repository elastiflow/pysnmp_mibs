# SNMP MIB module (CISCO-WAN-SRM-BERT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/stratacom_351/CISCO-WAN-SRM-BERT-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:08:17 2025
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

(axisDiagnostics,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "axisDiagnostics")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoWanSrmBertMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 31)
)
if mibBuilder.loadTexts:
    ciscoWanSrmBertMIB.setRevisions(
        ("2002-08-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bert_ObjectIdentity = ObjectIdentity
bert = _Bert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1)
)


class _BertControl_Type(Integer32):
    """Custom type bertControl based on Integer32"""
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
        *(("acquireBert", 1),
          ("releaseBert", 2),
          ("cnfBert", 3),
          ("startBert", 4),
          ("modBert", 5),
          ("delBert", 6))
    )


_BertControl_Type.__name__ = "Integer32"
_BertControl_Object = MibScalar
bertControl = _BertControl_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 1),
    _BertControl_Type()
)
bertControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertControl.setStatus("current")


class _BertResourceStatus_Type(Integer32):
    """Custom type bertResourceStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("free", 1),
          ("inUse", 2),
          ("cleanupPending", 3))
    )


_BertResourceStatus_Type.__name__ = "Integer32"
_BertResourceStatus_Object = MibScalar
bertResourceStatus = _BertResourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 2),
    _BertResourceStatus_Type()
)
bertResourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertResourceStatus.setStatus("current")
_BertOwner_Type = DisplayString
_BertOwner_Object = MibScalar
bertOwner = _BertOwner_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 3),
    _BertOwner_Type()
)
bertOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertOwner.setStatus("current")
_BertUserId_Type = DisplayString
_BertUserId_Object = MibScalar
bertUserId = _BertUserId_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 4),
    _BertUserId_Type()
)
bertUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertUserId.setStatus("current")


class _BertStatus_Type(Integer32):
    """Custom type bertStatus based on Integer32"""
    defaultValue = 1

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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("bertInSync", 2),
          ("bertOutOfSync", 3),
          ("searchingDDSCommands", 4),
          ("farEndInLoop", 5),
          ("facilityInLoop", 6),
          ("portFacilityFifoFault", 7),
          ("portFacilityFifoOutOfSync", 8),
          ("metallicInLoop", 9),
          ("bertFailed", 10))
    )


_BertStatus_Type.__name__ = "Integer32"
_BertStatus_Object = MibScalar
bertStatus = _BertStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 5),
    _BertStatus_Type()
)
bertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertStatus.setStatus("current")


class _BertSlotNumber_Type(Integer32):
    """Custom type bertSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BertSlotNumber_Type.__name__ = "Integer32"
_BertSlotNumber_Object = MibScalar
bertSlotNumber = _BertSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 6),
    _BertSlotNumber_Type()
)
bertSlotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertSlotNumber.setStatus("current")


class _BertTestMedium_Type(Integer32):
    """Custom type bertTestMedium based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("line", 2))
    )


_BertTestMedium_Type.__name__ = "Integer32"
_BertTestMedium_Object = MibScalar
bertTestMedium = _BertTestMedium_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 7),
    _BertTestMedium_Type()
)
bertTestMedium.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertTestMedium.setStatus("current")
_BertPort_Type = Integer32
_BertPort_Object = MibScalar
bertPort = _BertPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 8),
    _BertPort_Type()
)
bertPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertPort.setStatus("current")
_BertLine_Type = Integer32
_BertLine_Object = MibScalar
bertLine = _BertLine_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 9),
    _BertLine_Type()
)
bertLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertLine.setStatus("current")


class _BertMode_Type(Integer32):
    """Custom type bertMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bertPatternTest", 1),
          ("ddsSeek", 2),
          ("loopback", 3))
    )


_BertMode_Type.__name__ = "Integer32"
_BertMode_Object = MibScalar
bertMode = _BertMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 10),
    _BertMode_Type()
)
bertMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertMode.setStatus("current")


class _BertDeviceToLoop_Type(Integer32):
    """Custom type bertDeviceToLoop based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("noLatchOCUwith1", 1),
          ("noLatchOCUwitout1", 2),
          ("noLatchCSU", 3),
          ("noLatchDSU", 4),
          ("latchDS0Drop", 5),
          ("latchDS0Line", 6),
          ("latchOCU", 7),
          ("latchCSU", 8),
          ("latchDSU", 9),
          ("latchHL96", 10),
          ("v54Polynomial", 11),
          ("inband", 12),
          ("esf", 13),
          ("metallic", 14),
          ("noDevice", 15),
          ("smartJackInband", 16))
    )


_BertDeviceToLoop_Type.__name__ = "Integer32"
_BertDeviceToLoop_Object = MibScalar
bertDeviceToLoop = _BertDeviceToLoop_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 11),
    _BertDeviceToLoop_Type()
)
bertDeviceToLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertDeviceToLoop.setStatus("current")


class _BertDS0DPIterationCount_Type(Integer32):
    """Custom type bertDS0DPIterationCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_BertDS0DPIterationCount_Type.__name__ = "Integer32"
_BertDS0DPIterationCount_Object = MibScalar
bertDS0DPIterationCount = _BertDS0DPIterationCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 12),
    _BertDS0DPIterationCount_Type()
)
bertDS0DPIterationCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertDS0DPIterationCount.setStatus("current")


class _BertPattern_Type(Integer32):
    """Custom type bertPattern based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("allZeros", 1),
          ("allOnes", 2),
          ("alternateONeZero", 3),
          ("doubleOneZero", 4),
          ("fifteenBit", 5),
          ("twentyBit", 6),
          ("twentyBitQRSS", 7),
          ("twentythreeBit", 8),
          ("oneInEight", 9),
          ("threeIntwentyfour", 10),
          ("dds-1", 11),
          ("dds-2", 12),
          ("dds-3", 13),
          ("dds-4", 14),
          ("dds-5", 15),
          ("nineBit", 16),
          ("elevenBit", 17))
    )


_BertPattern_Type.__name__ = "Integer32"
_BertPattern_Object = MibScalar
bertPattern = _BertPattern_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 13),
    _BertPattern_Type()
)
bertPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertPattern.setStatus("current")


class _BertLoopback_Type(Integer32):
    """Custom type bertLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("farEndLoopback", 1),
          ("facilityLoopback", 2),
          ("metallicLoopback", 3))
    )


_BertLoopback_Type.__name__ = "Integer32"
_BertLoopback_Object = MibScalar
bertLoopback = _BertLoopback_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 14),
    _BertLoopback_Type()
)
bertLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertLoopback.setStatus("current")


class _BertLoopbackOperation_Type(Integer32):
    """Custom type bertLoopbackOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopUp", 1),
          ("loopDown", 2))
    )


_BertLoopbackOperation_Type.__name__ = "Integer32"
_BertLoopbackOperation_Object = MibScalar
bertLoopbackOperation = _BertLoopbackOperation_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 15),
    _BertLoopbackOperation_Type()
)
bertLoopbackOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bertLoopbackOperation.setStatus("current")


class _BertDS0Speed_Type(Integer32):
    """Custom type bertDS0Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speed56k", 1),
          ("speed64k", 2))
    )


_BertDS0Speed_Type.__name__ = "Integer32"
_BertDS0Speed_Object = MibScalar
bertDS0Speed = _BertDS0Speed_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 16),
    _BertDS0Speed_Type()
)
bertDS0Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertDS0Speed.setStatus("current")
_BertTimeSlots_Type = Integer32
_BertTimeSlots_Object = MibScalar
bertTimeSlots = _BertTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 17),
    _BertTimeSlots_Type()
)
bertTimeSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTimeSlots.setStatus("current")


class _BertStartTime_Type(DisplayString):
    """Custom type bertStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_BertStartTime_Type.__name__ = "DisplayString"
_BertStartTime_Object = MibScalar
bertStartTime = _BertStartTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 18),
    _BertStartTime_Type()
)
bertStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertStartTime.setStatus("current")


class _BertStartDate_Type(DisplayString):
    """Custom type bertStartDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixedLength = 10


_BertStartDate_Type.__name__ = "DisplayString"
_BertStartDate_Object = MibScalar
bertStartDate = _BertStartDate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 19),
    _BertStartDate_Type()
)
bertStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertStartDate.setStatus("current")
_BertBitCount_Type = Integer32
_BertBitCount_Object = MibScalar
bertBitCount = _BertBitCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 20),
    _BertBitCount_Type()
)
bertBitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertBitCount.setStatus("current")
_BertBitErrorCount_Type = Integer32
_BertBitErrorCount_Object = MibScalar
bertBitErrorCount = _BertBitErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 21),
    _BertBitErrorCount_Type()
)
bertBitErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertBitErrorCount.setStatus("current")
_BertErrorInjectCount_Type = Integer32
_BertErrorInjectCount_Object = MibScalar
bertErrorInjectCount = _BertErrorInjectCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 22),
    _BertErrorInjectCount_Type()
)
bertErrorInjectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertErrorInjectCount.setStatus("current")


class _BertCleanupAction_Type(Integer32):
    """Custom type bertCleanupAction based on Integer32"""
    defaultValue = 1

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
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("smCleanup", 2),
          ("latchDS0DropLoopdown", 3),
          ("latchDS0LineLoopdown", 4),
          ("latchOCULoopdown", 5),
          ("latchCSULoopdown", 6),
          ("latchDSULoopdown", 7),
          ("latchHL96Loopdown", 8),
          ("v54PolynomialLoopdown", 9),
          ("inbandLoopdown", 10),
          ("esfLoopdown", 11),
          ("facilityLoopdown", 12),
          ("metallicLoopdown", 13),
          ("smartJackInbandLoopdown", 14))
    )


_BertCleanupAction_Type.__name__ = "Integer32"
_BertCleanupAction_Object = MibScalar
bertCleanupAction = _BertCleanupAction_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 23),
    _BertCleanupAction_Type()
)
bertCleanupAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertCleanupAction.setStatus("current")


class _BertAbortReason_Type(Integer32):
    """Custom type bertAbortReason based on Integer32"""
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
        *(("ascStateChange", 1),
          ("smStateChange", 2),
          ("srmStateChange", 3),
          ("coreCardSwitch", 4),
          ("smRedundancySwitch", 5))
    )


_BertAbortReason_Type.__name__ = "Integer32"
_BertAbortReason_Object = MibScalar
bertAbortReason = _BertAbortReason_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 24),
    _BertAbortReason_Type()
)
bertAbortReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertAbortReason.setStatus("current")


class _BertDDSSeekResultsTableFirstIndex_Type(Integer32):
    """Custom type bertDDSSeekResultsTableFirstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_BertDDSSeekResultsTableFirstIndex_Type.__name__ = "Integer32"
_BertDDSSeekResultsTableFirstIndex_Object = MibScalar
bertDDSSeekResultsTableFirstIndex = _BertDDSSeekResultsTableFirstIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 25),
    _BertDDSSeekResultsTableFirstIndex_Type()
)
bertDDSSeekResultsTableFirstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertDDSSeekResultsTableFirstIndex.setStatus("current")


class _BertDDSSeekResultsTableLastIndex_Type(Integer32):
    """Custom type bertDDSSeekResultsTableLastIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_BertDDSSeekResultsTableLastIndex_Type.__name__ = "Integer32"
_BertDDSSeekResultsTableLastIndex_Object = MibScalar
bertDDSSeekResultsTableLastIndex = _BertDDSSeekResultsTableLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 26),
    _BertDDSSeekResultsTableLastIndex_Type()
)
bertDDSSeekResultsTableLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertDDSSeekResultsTableLastIndex.setStatus("current")
_BertDDSSeekResultsTable_Object = MibTable
bertDDSSeekResultsTable = _BertDDSSeekResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 27)
)
if mibBuilder.loadTexts:
    bertDDSSeekResultsTable.setStatus("current")
_BertDDSSeekResultsTableEntry_Object = MibTableRow
bertDDSSeekResultsTableEntry = _BertDDSSeekResultsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 27, 1)
)
bertDDSSeekResultsTableEntry.setIndexNames(
    (0, "CISCO-WAN-SRM-BERT-MIB", "bertDDSSeekResultsTableIndex"),
)
if mibBuilder.loadTexts:
    bertDDSSeekResultsTableEntry.setStatus("current")


class _BertDDSSeekResultsTableIndex_Type(Integer32):
    """Custom type bertDDSSeekResultsTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_BertDDSSeekResultsTableIndex_Type.__name__ = "Integer32"
_BertDDSSeekResultsTableIndex_Object = MibTableColumn
bertDDSSeekResultsTableIndex = _BertDDSSeekResultsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 27, 1, 1),
    _BertDDSSeekResultsTableIndex_Type()
)
bertDDSSeekResultsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertDDSSeekResultsTableIndex.setStatus("current")


class _BertDDSCode_Type(Integer32):
    """Custom type bertDDSCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              24,
              26,
              28,
              30,
              40,
              42,
              44,
              50,
              58,
              86,
              90,
              108,
              114,
              120,
              126)
        )
    )
    namedValues = NamedValues(
        *(("block", 10),
          ("unassignedMuxChannel", 24),
          ("muxOutOfSync", 26),
          ("test", 28),
          ("abnormalStationCondition", 30),
          ("channelLoopback", 40),
          ("ocuLoopback", 42),
          ("dsuLoopback", 44),
          ("unnamed", 50),
          ("transitionInProgress", 58),
          ("loopbackEnable", 86),
          ("farEndVoice", 90),
          ("testAlert", 108),
          ("mjuAlert", 114),
          ("release", 120),
          ("idle", 126))
    )


_BertDDSCode_Type.__name__ = "Integer32"
_BertDDSCode_Object = MibTableColumn
bertDDSCode = _BertDDSCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 27, 1, 2),
    _BertDDSCode_Type()
)
bertDDSCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertDDSCode.setStatus("current")
_BertSupportedTestsTable_Object = MibTable
bertSupportedTestsTable = _BertSupportedTestsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28)
)
if mibBuilder.loadTexts:
    bertSupportedTestsTable.setStatus("current")
_BertSupportedTestsTableEntry_Object = MibTableRow
bertSupportedTestsTableEntry = _BertSupportedTestsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28, 1)
)
bertSupportedTestsTableEntry.setIndexNames(
    (0, "CISCO-WAN-SRM-BERT-MIB", "bertSupportedTestsTableIndex"),
)
if mibBuilder.loadTexts:
    bertSupportedTestsTableEntry.setStatus("current")


class _BertSupportedTestsTableIndex_Type(Integer32):
    """Custom type bertSupportedTestsTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BertSupportedTestsTableIndex_Type.__name__ = "Integer32"
_BertSupportedTestsTableIndex_Object = MibTableColumn
bertSupportedTestsTableIndex = _BertSupportedTestsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28, 1, 1),
    _BertSupportedTestsTableIndex_Type()
)
bertSupportedTestsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertSupportedTestsTableIndex.setStatus("current")


class _BertSupportFlag_Type(Integer32):
    """Custom type bertSupportFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_BertSupportFlag_Type.__name__ = "Integer32"
_BertSupportFlag_Object = MibTableColumn
bertSupportFlag = _BertSupportFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28, 1, 2),
    _BertSupportFlag_Type()
)
bertSupportFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertSupportFlag.setStatus("current")
_BertTestMediumMask_Type = Integer32
_BertTestMediumMask_Object = MibTableColumn
bertTestMediumMask = _BertTestMediumMask_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28, 1, 3),
    _BertTestMediumMask_Type()
)
bertTestMediumMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertTestMediumMask.setStatus("current")
_BertModeMask_Type = Integer32
_BertModeMask_Object = MibTableColumn
bertModeMask = _BertModeMask_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28, 1, 4),
    _BertModeMask_Type()
)
bertModeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertModeMask.setStatus("current")
_BertDeviceToLoopMask_Type = Integer32
_BertDeviceToLoopMask_Object = MibTableColumn
bertDeviceToLoopMask = _BertDeviceToLoopMask_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28, 1, 5),
    _BertDeviceToLoopMask_Type()
)
bertDeviceToLoopMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertDeviceToLoopMask.setStatus("current")
_BertPatternMask_Type = Integer32
_BertPatternMask_Object = MibTableColumn
bertPatternMask = _BertPatternMask_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28, 1, 6),
    _BertPatternMask_Type()
)
bertPatternMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertPatternMask.setStatus("current")
_BertLoopbackMask_Type = Integer32
_BertLoopbackMask_Object = MibTableColumn
bertLoopbackMask = _BertLoopbackMask_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28, 1, 7),
    _BertLoopbackMask_Type()
)
bertLoopbackMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertLoopbackMask.setStatus("current")


class _BertCardT1E1Type_Type(Integer32):
    """Custom type bertCardT1E1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t1", 1),
          ("e1", 2))
    )


_BertCardT1E1Type_Type.__name__ = "Integer32"
_BertCardT1E1Type_Object = MibTableColumn
bertCardT1E1Type = _BertCardT1E1Type_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 6, 1, 28, 1, 8),
    _BertCardT1E1Type_Type()
)
bertCardT1E1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bertCardT1E1Type.setStatus("current")
_CiscoWanSrmBertMIBConformance_ObjectIdentity = ObjectIdentity
ciscoWanSrmBertMIBConformance = _CiscoWanSrmBertMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 31, 2)
)
_CiscoWanSrmBertMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWanSrmBertMIBGroups = _CiscoWanSrmBertMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 31, 2, 1)
)
_CiscoWanSrmBertMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWanSrmBertMIBCompliances = _CiscoWanSrmBertMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 31, 2, 2)
)

# Managed Objects groups

ciscoWanSrmBertConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 31, 2, 1, 1)
)
ciscoWanSrmBertConfGroup.setObjects(
      *(("CISCO-WAN-SRM-BERT-MIB", "bertControl"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertResourceStatus"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertOwner"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertUserId"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertStatus"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertSlotNumber"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertTestMedium"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertPort"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertLine"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertMode"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertDeviceToLoop"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertDS0DPIterationCount"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertPattern"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertLoopback"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertLoopbackOperation"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertDS0Speed"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertTimeSlots"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertStartTime"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertStartDate"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertBitCount"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertBitErrorCount"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertErrorInjectCount"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertCleanupAction"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertAbortReason"))
)
if mibBuilder.loadTexts:
    ciscoWanSrmBertConfGroup.setStatus("current")

ciscoWanSrmBertTestResultsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 31, 2, 1, 2)
)
ciscoWanSrmBertTestResultsGroup.setObjects(
      *(("CISCO-WAN-SRM-BERT-MIB", "bertSupportedTestsTableIndex"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertSupportFlag"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertTestMediumMask"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertModeMask"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertDeviceToLoopMask"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertPatternMask"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertLoopbackMask"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertCardT1E1Type"))
)
if mibBuilder.loadTexts:
    ciscoWanSrmBertTestResultsGroup.setStatus("current")

ciscoWanSrmBertDDSResultsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 31, 2, 1, 3)
)
ciscoWanSrmBertDDSResultsGroup.setObjects(
      *(("CISCO-WAN-SRM-BERT-MIB", "bertDDSSeekResultsTableFirstIndex"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertDDSSeekResultsTableLastIndex"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertDDSSeekResultsTableIndex"),
        ("CISCO-WAN-SRM-BERT-MIB", "bertDDSCode"))
)
if mibBuilder.loadTexts:
    ciscoWanSrmBertDDSResultsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWanSrmBertCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 31, 2, 2, 1)
)
ciscoWanSrmBertCompliance.setObjects(
    ("CISCO-WAN-SRM-BERT-MIB", "ciscoWanSrmBertConfGroup")
)
if mibBuilder.loadTexts:
    ciscoWanSrmBertCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-SRM-BERT-MIB",
    **{"bert": bert,
       "bertControl": bertControl,
       "bertResourceStatus": bertResourceStatus,
       "bertOwner": bertOwner,
       "bertUserId": bertUserId,
       "bertStatus": bertStatus,
       "bertSlotNumber": bertSlotNumber,
       "bertTestMedium": bertTestMedium,
       "bertPort": bertPort,
       "bertLine": bertLine,
       "bertMode": bertMode,
       "bertDeviceToLoop": bertDeviceToLoop,
       "bertDS0DPIterationCount": bertDS0DPIterationCount,
       "bertPattern": bertPattern,
       "bertLoopback": bertLoopback,
       "bertLoopbackOperation": bertLoopbackOperation,
       "bertDS0Speed": bertDS0Speed,
       "bertTimeSlots": bertTimeSlots,
       "bertStartTime": bertStartTime,
       "bertStartDate": bertStartDate,
       "bertBitCount": bertBitCount,
       "bertBitErrorCount": bertBitErrorCount,
       "bertErrorInjectCount": bertErrorInjectCount,
       "bertCleanupAction": bertCleanupAction,
       "bertAbortReason": bertAbortReason,
       "bertDDSSeekResultsTableFirstIndex": bertDDSSeekResultsTableFirstIndex,
       "bertDDSSeekResultsTableLastIndex": bertDDSSeekResultsTableLastIndex,
       "bertDDSSeekResultsTable": bertDDSSeekResultsTable,
       "bertDDSSeekResultsTableEntry": bertDDSSeekResultsTableEntry,
       "bertDDSSeekResultsTableIndex": bertDDSSeekResultsTableIndex,
       "bertDDSCode": bertDDSCode,
       "bertSupportedTestsTable": bertSupportedTestsTable,
       "bertSupportedTestsTableEntry": bertSupportedTestsTableEntry,
       "bertSupportedTestsTableIndex": bertSupportedTestsTableIndex,
       "bertSupportFlag": bertSupportFlag,
       "bertTestMediumMask": bertTestMediumMask,
       "bertModeMask": bertModeMask,
       "bertDeviceToLoopMask": bertDeviceToLoopMask,
       "bertPatternMask": bertPatternMask,
       "bertLoopbackMask": bertLoopbackMask,
       "bertCardT1E1Type": bertCardT1E1Type,
       "ciscoWanSrmBertMIB": ciscoWanSrmBertMIB,
       "ciscoWanSrmBertMIBConformance": ciscoWanSrmBertMIBConformance,
       "ciscoWanSrmBertMIBGroups": ciscoWanSrmBertMIBGroups,
       "ciscoWanSrmBertConfGroup": ciscoWanSrmBertConfGroup,
       "ciscoWanSrmBertTestResultsGroup": ciscoWanSrmBertTestResultsGroup,
       "ciscoWanSrmBertDDSResultsGroup": ciscoWanSrmBertDDSResultsGroup,
       "ciscoWanSrmBertMIBCompliances": ciscoWanSrmBertMIBCompliances,
       "ciscoWanSrmBertCompliance": ciscoWanSrmBertCompliance}
)
