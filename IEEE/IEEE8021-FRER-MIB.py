# SNMP MIB module (IEEE8021-FRER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IEEE/IEEE8021-FRER-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:10:49 2025
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

(Ieee8021CBLanPathIdType,
 Ieee8021CBTaggedType,
 Ieee8021CBVlanIdentifier,
 ieee8021StreamIdStreamIdHandle) = mibBuilder.importSymbols(
    "IEEE8021-STREAM-IDENTIFICATION-MIB",
    "Ieee8021CBLanPathIdType",
    "Ieee8021CBTaggedType",
    "Ieee8021CBVlanIdentifier",
    "ieee8021StreamIdStreamIdHandle")

(ieee802dot1mibs,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "ieee802dot1mibs")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

(AutonomousType,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

ieee8021FrerMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35)
)
if mibBuilder.loadTexts:
    ieee8021FrerMib.setRevisions(
        ("2021-12-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Ieee8021CBSequenceRecoveryAlgorithm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              256)
        )
    )
    namedValues = NamedValues(
        *(("vectorAlgorithm", 0),
          ("matchAlgorithm", 1),
          ("nonIEEESpecified", 256))
    )



class Ieee8021CBSequenceEncodeDecodeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              256)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("rTAG", 1),
          ("hsrSequenceTag", 2),
          ("prpSequenceTag", 3),
          ("nonIEEESpecified", 256))
    )



# MIB Managed Objects in the order of their OIDs

_Ieee8021FrerNotifications_ObjectIdentity = ObjectIdentity
ieee8021FrerNotifications = _Ieee8021FrerNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 0)
)
_Ieee8021FrerObjects_ObjectIdentity = ObjectIdentity
ieee8021FrerObjects = _Ieee8021FrerObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 1)
)
_Ieee8021FrerSequenceGeneration_ObjectIdentity = ObjectIdentity
ieee8021FrerSequenceGeneration = _Ieee8021FrerSequenceGeneration_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 1)
)
_Ieee8021FrerSequenceGenerationTable_Object = MibTable
ieee8021FrerSequenceGenerationTable = _Ieee8021FrerSequenceGenerationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceGenerationTable.setStatus("current")
_Ieee8021FrerSequenceGenerationEntry_Object = MibTableRow
ieee8021FrerSequenceGenerationEntry = _Ieee8021FrerSequenceGenerationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 1, 1, 1)
)
ieee8021FrerSequenceGenerationEntry.setIndexNames(
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceGenerationIndex"),
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceGenerationEntry.setStatus("current")
_Ieee8021FrerSequenceGenerationIndex_Type = Unsigned32
_Ieee8021FrerSequenceGenerationIndex_Object = MibTableColumn
ieee8021FrerSequenceGenerationIndex = _Ieee8021FrerSequenceGenerationIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 1, 1, 1, 1),
    _Ieee8021FrerSequenceGenerationIndex_Type()
)
ieee8021FrerSequenceGenerationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceGenerationIndex.setStatus("current")
_Ieee8021FrerSequenceGenerationStreamList_Type = AutonomousType
_Ieee8021FrerSequenceGenerationStreamList_Object = MibTableColumn
ieee8021FrerSequenceGenerationStreamList = _Ieee8021FrerSequenceGenerationStreamList_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 1, 1, 1, 2),
    _Ieee8021FrerSequenceGenerationStreamList_Type()
)
ieee8021FrerSequenceGenerationStreamList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceGenerationStreamList.setStatus("current")
_Ieee8021FrerSequenceGenerationDirection_Type = TruthValue
_Ieee8021FrerSequenceGenerationDirection_Object = MibTableColumn
ieee8021FrerSequenceGenerationDirection = _Ieee8021FrerSequenceGenerationDirection_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 1, 1, 1, 3),
    _Ieee8021FrerSequenceGenerationDirection_Type()
)
ieee8021FrerSequenceGenerationDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceGenerationDirection.setStatus("current")
_Ieee8021FrerSequenceGenerationReset_Type = TruthValue
_Ieee8021FrerSequenceGenerationReset_Object = MibTableColumn
ieee8021FrerSequenceGenerationReset = _Ieee8021FrerSequenceGenerationReset_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 1, 1, 1, 4),
    _Ieee8021FrerSequenceGenerationReset_Type()
)
ieee8021FrerSequenceGenerationReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceGenerationReset.setStatus("current")
_Ieee8021FrerSequenceGenerationHandleList_ObjectIdentity = ObjectIdentity
ieee8021FrerSequenceGenerationHandleList = _Ieee8021FrerSequenceGenerationHandleList_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 2)
)
_Ieee8021FrerSequenceGenerationHandleListTable_Object = MibTable
ieee8021FrerSequenceGenerationHandleListTable = _Ieee8021FrerSequenceGenerationHandleListTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceGenerationHandleListTable.setStatus("current")
_Ieee8021FrerSequenceGenerationHandleListEntry_Object = MibTableRow
ieee8021FrerSequenceGenerationHandleListEntry = _Ieee8021FrerSequenceGenerationHandleListEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 2, 2, 1)
)
ieee8021FrerSequenceGenerationHandleListEntry.setIndexNames(
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceGenerationIndex"),
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceGenerationHandleListIndex"),
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceGenerationHandleListEntry.setStatus("current")
_Ieee8021FrerSequenceGenerationHandleListIndex_Type = Unsigned32
_Ieee8021FrerSequenceGenerationHandleListIndex_Object = MibTableColumn
ieee8021FrerSequenceGenerationHandleListIndex = _Ieee8021FrerSequenceGenerationHandleListIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 2, 2, 1, 1),
    _Ieee8021FrerSequenceGenerationHandleListIndex_Type()
)
ieee8021FrerSequenceGenerationHandleListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceGenerationHandleListIndex.setStatus("current")
_Ieee8021FrerSequenceGenerationStreamHandle_Type = VariablePointer
_Ieee8021FrerSequenceGenerationStreamHandle_Object = MibTableColumn
ieee8021FrerSequenceGenerationStreamHandle = _Ieee8021FrerSequenceGenerationStreamHandle_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 2, 2, 1, 2),
    _Ieee8021FrerSequenceGenerationStreamHandle_Type()
)
ieee8021FrerSequenceGenerationStreamHandle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceGenerationStreamHandle.setStatus("current")
_Ieee8021FrerSequenceGenerationHandleListStatus_Type = RowStatus
_Ieee8021FrerSequenceGenerationHandleListStatus_Object = MibTableColumn
ieee8021FrerSequenceGenerationHandleListStatus = _Ieee8021FrerSequenceGenerationHandleListStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 2, 2, 1, 3),
    _Ieee8021FrerSequenceGenerationHandleListStatus_Type()
)
ieee8021FrerSequenceGenerationHandleListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceGenerationHandleListStatus.setStatus("current")
_Ieee8021FrerSequenceRecovery_ObjectIdentity = ObjectIdentity
ieee8021FrerSequenceRecovery = _Ieee8021FrerSequenceRecovery_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3)
)
_Ieee8021FrerSequenceRecoveryTable_Object = MibTable
ieee8021FrerSequenceRecoveryTable = _Ieee8021FrerSequenceRecoveryTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryTable.setStatus("current")
_Ieee8021FrerSequenceRecoveryEntry_Object = MibTableRow
ieee8021FrerSequenceRecoveryEntry = _Ieee8021FrerSequenceRecoveryEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1)
)
ieee8021FrerSequenceRecoveryEntry.setIndexNames(
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryIndex"),
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryEntry.setStatus("current")
_Ieee8021FrerSequenceRecoveryIndex_Type = Unsigned32
_Ieee8021FrerSequenceRecoveryIndex_Object = MibTableColumn
ieee8021FrerSequenceRecoveryIndex = _Ieee8021FrerSequenceRecoveryIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 1),
    _Ieee8021FrerSequenceRecoveryIndex_Type()
)
ieee8021FrerSequenceRecoveryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryIndex.setStatus("current")
_Ieee8021FrerSequenceRecoveryStreamList_Type = AutonomousType
_Ieee8021FrerSequenceRecoveryStreamList_Object = MibTableColumn
ieee8021FrerSequenceRecoveryStreamList = _Ieee8021FrerSequenceRecoveryStreamList_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 2),
    _Ieee8021FrerSequenceRecoveryStreamList_Type()
)
ieee8021FrerSequenceRecoveryStreamList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryStreamList.setStatus("current")
_Ieee8021FrerSequenceRecoveryPortList_Type = AutonomousType
_Ieee8021FrerSequenceRecoveryPortList_Object = MibTableColumn
ieee8021FrerSequenceRecoveryPortList = _Ieee8021FrerSequenceRecoveryPortList_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 3),
    _Ieee8021FrerSequenceRecoveryPortList_Type()
)
ieee8021FrerSequenceRecoveryPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryPortList.setStatus("current")
_Ieee8021FrerSequenceRecoveryDirection_Type = TruthValue
_Ieee8021FrerSequenceRecoveryDirection_Object = MibTableColumn
ieee8021FrerSequenceRecoveryDirection = _Ieee8021FrerSequenceRecoveryDirection_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 4),
    _Ieee8021FrerSequenceRecoveryDirection_Type()
)
ieee8021FrerSequenceRecoveryDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryDirection.setStatus("current")
_Ieee8021FrerSequenceRecoveryReset_Type = TruthValue
_Ieee8021FrerSequenceRecoveryReset_Object = MibTableColumn
ieee8021FrerSequenceRecoveryReset = _Ieee8021FrerSequenceRecoveryReset_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 5),
    _Ieee8021FrerSequenceRecoveryReset_Type()
)
ieee8021FrerSequenceRecoveryReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryReset.setStatus("current")


class _Ieee8021FrerSequenceRecoveryAlgorithm_Type(Ieee8021CBSequenceRecoveryAlgorithm):
    """Custom type ieee8021FrerSequenceRecoveryAlgorithm based on Ieee8021CBSequenceRecoveryAlgorithm"""
    defaultValue = 0


_Ieee8021FrerSequenceRecoveryAlgorithm_Type.__name__ = "Ieee8021CBSequenceRecoveryAlgorithm"
_Ieee8021FrerSequenceRecoveryAlgorithm_Object = MibTableColumn
ieee8021FrerSequenceRecoveryAlgorithm = _Ieee8021FrerSequenceRecoveryAlgorithm_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 6),
    _Ieee8021FrerSequenceRecoveryAlgorithm_Type()
)
ieee8021FrerSequenceRecoveryAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryAlgorithm.setStatus("current")


class _Ieee8021FrerSequenceRecoveryAlgorithmOUI_Type(OctetString):
    """Custom type ieee8021FrerSequenceRecoveryAlgorithmOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_Ieee8021FrerSequenceRecoveryAlgorithmOUI_Type.__name__ = "OctetString"
_Ieee8021FrerSequenceRecoveryAlgorithmOUI_Object = MibTableColumn
ieee8021FrerSequenceRecoveryAlgorithmOUI = _Ieee8021FrerSequenceRecoveryAlgorithmOUI_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 7),
    _Ieee8021FrerSequenceRecoveryAlgorithmOUI_Type()
)
ieee8021FrerSequenceRecoveryAlgorithmOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryAlgorithmOUI.setStatus("current")


class _Ieee8021FrerSequenceCustomRecoveryAlgorithm_Type(Integer32):
    """Custom type ieee8021FrerSequenceCustomRecoveryAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2147483647),
    )


_Ieee8021FrerSequenceCustomRecoveryAlgorithm_Type.__name__ = "Integer32"
_Ieee8021FrerSequenceCustomRecoveryAlgorithm_Object = MibTableColumn
ieee8021FrerSequenceCustomRecoveryAlgorithm = _Ieee8021FrerSequenceCustomRecoveryAlgorithm_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 8),
    _Ieee8021FrerSequenceCustomRecoveryAlgorithm_Type()
)
ieee8021FrerSequenceCustomRecoveryAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceCustomRecoveryAlgorithm.setStatus("current")


class _Ieee8021FrerSequenceCustomRecoveryAlgorithmOUI_Type(OctetString):
    """Custom type ieee8021FrerSequenceCustomRecoveryAlgorithmOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_Ieee8021FrerSequenceCustomRecoveryAlgorithmOUI_Type.__name__ = "OctetString"
_Ieee8021FrerSequenceCustomRecoveryAlgorithmOUI_Object = MibTableColumn
ieee8021FrerSequenceCustomRecoveryAlgorithmOUI = _Ieee8021FrerSequenceCustomRecoveryAlgorithmOUI_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 9),
    _Ieee8021FrerSequenceCustomRecoveryAlgorithmOUI_Type()
)
ieee8021FrerSequenceCustomRecoveryAlgorithmOUI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceCustomRecoveryAlgorithmOUI.setStatus("current")
_Ieee8021FrerSequenceRecoveryHistoryLength_Type = Integer32
_Ieee8021FrerSequenceRecoveryHistoryLength_Object = MibTableColumn
ieee8021FrerSequenceRecoveryHistoryLength = _Ieee8021FrerSequenceRecoveryHistoryLength_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 10),
    _Ieee8021FrerSequenceRecoveryHistoryLength_Type()
)
ieee8021FrerSequenceRecoveryHistoryLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryHistoryLength.setStatus("current")
_Ieee8021FrerSequenceRecoveryResetMSec_Type = Unsigned32
_Ieee8021FrerSequenceRecoveryResetMSec_Object = MibTableColumn
ieee8021FrerSequenceRecoveryResetMSec = _Ieee8021FrerSequenceRecoveryResetMSec_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 11),
    _Ieee8021FrerSequenceRecoveryResetMSec_Type()
)
ieee8021FrerSequenceRecoveryResetMSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryResetMSec.setStatus("current")
_Ieee8021FrerSequenceRecoveryInvalidSequenceValue_Type = Unsigned32
_Ieee8021FrerSequenceRecoveryInvalidSequenceValue_Object = MibTableColumn
ieee8021FrerSequenceRecoveryInvalidSequenceValue = _Ieee8021FrerSequenceRecoveryInvalidSequenceValue_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 12),
    _Ieee8021FrerSequenceRecoveryInvalidSequenceValue_Type()
)
ieee8021FrerSequenceRecoveryInvalidSequenceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryInvalidSequenceValue.setStatus("current")


class _Ieee8021FrerSequenceRecoveryTakeNoSequence_Type(TruthValue):
    """Custom type ieee8021FrerSequenceRecoveryTakeNoSequence based on TruthValue"""
    defaultValue = 2


_Ieee8021FrerSequenceRecoveryTakeNoSequence_Type.__name__ = "TruthValue"
_Ieee8021FrerSequenceRecoveryTakeNoSequence_Object = MibTableColumn
ieee8021FrerSequenceRecoveryTakeNoSequence = _Ieee8021FrerSequenceRecoveryTakeNoSequence_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 13),
    _Ieee8021FrerSequenceRecoveryTakeNoSequence_Type()
)
ieee8021FrerSequenceRecoveryTakeNoSequence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryTakeNoSequence.setStatus("current")
_Ieee8021FrerSequenceRecoveryIndividualRecovery_Type = TruthValue
_Ieee8021FrerSequenceRecoveryIndividualRecovery_Object = MibTableColumn
ieee8021FrerSequenceRecoveryIndividualRecovery = _Ieee8021FrerSequenceRecoveryIndividualRecovery_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 14),
    _Ieee8021FrerSequenceRecoveryIndividualRecovery_Type()
)
ieee8021FrerSequenceRecoveryIndividualRecovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryIndividualRecovery.setStatus("current")
_Ieee8021FrerSequenceRecoveryLatentErrorDetection_Type = TruthValue
_Ieee8021FrerSequenceRecoveryLatentErrorDetection_Object = MibTableColumn
ieee8021FrerSequenceRecoveryLatentErrorDetection = _Ieee8021FrerSequenceRecoveryLatentErrorDetection_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 15),
    _Ieee8021FrerSequenceRecoveryLatentErrorDetection_Type()
)
ieee8021FrerSequenceRecoveryLatentErrorDetection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryLatentErrorDetection.setStatus("current")
_Ieee8021FrerSequenceRecoveryLatentErrorDifference_Type = Integer32
_Ieee8021FrerSequenceRecoveryLatentErrorDifference_Object = MibTableColumn
ieee8021FrerSequenceRecoveryLatentErrorDifference = _Ieee8021FrerSequenceRecoveryLatentErrorDifference_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 16),
    _Ieee8021FrerSequenceRecoveryLatentErrorDifference_Type()
)
ieee8021FrerSequenceRecoveryLatentErrorDifference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryLatentErrorDifference.setStatus("current")


class _Ieee8021FrerSequenceRecoveryLatentErrorPeriod_Type(Integer32):
    """Custom type ieee8021FrerSequenceRecoveryLatentErrorPeriod based on Integer32"""
    defaultValue = 2000


_Ieee8021FrerSequenceRecoveryLatentErrorPeriod_Type.__name__ = "Integer32"
_Ieee8021FrerSequenceRecoveryLatentErrorPeriod_Object = MibTableColumn
ieee8021FrerSequenceRecoveryLatentErrorPeriod = _Ieee8021FrerSequenceRecoveryLatentErrorPeriod_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 17),
    _Ieee8021FrerSequenceRecoveryLatentErrorPeriod_Type()
)
ieee8021FrerSequenceRecoveryLatentErrorPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryLatentErrorPeriod.setStatus("current")
_Ieee8021FrerSequenceRecoveryLatentErrorPaths_Type = Integer32
_Ieee8021FrerSequenceRecoveryLatentErrorPaths_Object = MibTableColumn
ieee8021FrerSequenceRecoveryLatentErrorPaths = _Ieee8021FrerSequenceRecoveryLatentErrorPaths_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 18),
    _Ieee8021FrerSequenceRecoveryLatentErrorPaths_Type()
)
ieee8021FrerSequenceRecoveryLatentErrorPaths.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryLatentErrorPaths.setStatus("current")


class _Ieee8021FrerSequenceRecoveryLatentResetPeriod_Type(Integer32):
    """Custom type ieee8021FrerSequenceRecoveryLatentResetPeriod based on Integer32"""
    defaultValue = 30000


_Ieee8021FrerSequenceRecoveryLatentResetPeriod_Type.__name__ = "Integer32"
_Ieee8021FrerSequenceRecoveryLatentResetPeriod_Object = MibTableColumn
ieee8021FrerSequenceRecoveryLatentResetPeriod = _Ieee8021FrerSequenceRecoveryLatentResetPeriod_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 19),
    _Ieee8021FrerSequenceRecoveryLatentResetPeriod_Type()
)
ieee8021FrerSequenceRecoveryLatentResetPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryLatentResetPeriod.setStatus("current")
_Ieee8021FrerSequenceRecoveryStatus_Type = RowStatus
_Ieee8021FrerSequenceRecoveryStatus_Object = MibTableColumn
ieee8021FrerSequenceRecoveryStatus = _Ieee8021FrerSequenceRecoveryStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 3, 3, 1, 20),
    _Ieee8021FrerSequenceRecoveryStatus_Type()
)
ieee8021FrerSequenceRecoveryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryStatus.setStatus("current")
_Ieee8021FrerSequenceRecoveryHandleList_ObjectIdentity = ObjectIdentity
ieee8021FrerSequenceRecoveryHandleList = _Ieee8021FrerSequenceRecoveryHandleList_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 4)
)
_Ieee8021FrerSequenceRecoveryHandleListTable_Object = MibTable
ieee8021FrerSequenceRecoveryHandleListTable = _Ieee8021FrerSequenceRecoveryHandleListTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 4, 4)
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryHandleListTable.setStatus("current")
_Ieee8021FrerSequenceRecoveryHandleListEntry_Object = MibTableRow
ieee8021FrerSequenceRecoveryHandleListEntry = _Ieee8021FrerSequenceRecoveryHandleListEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 4, 4, 1)
)
ieee8021FrerSequenceRecoveryHandleListEntry.setIndexNames(
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryIndex"),
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryHandleListIndex"),
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryHandleListEntry.setStatus("current")
_Ieee8021FrerSequenceRecoveryHandleListIndex_Type = Unsigned32
_Ieee8021FrerSequenceRecoveryHandleListIndex_Object = MibTableColumn
ieee8021FrerSequenceRecoveryHandleListIndex = _Ieee8021FrerSequenceRecoveryHandleListIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 4, 4, 1, 1),
    _Ieee8021FrerSequenceRecoveryHandleListIndex_Type()
)
ieee8021FrerSequenceRecoveryHandleListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryHandleListIndex.setStatus("current")
_Ieee8021FrerSequenceRecoveryStreamHandle_Type = VariablePointer
_Ieee8021FrerSequenceRecoveryStreamHandle_Object = MibTableColumn
ieee8021FrerSequenceRecoveryStreamHandle = _Ieee8021FrerSequenceRecoveryStreamHandle_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 4, 4, 1, 2),
    _Ieee8021FrerSequenceRecoveryStreamHandle_Type()
)
ieee8021FrerSequenceRecoveryStreamHandle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryStreamHandle.setStatus("current")
_Ieee8021FrerSequenceRecoveryHandleListStatus_Type = RowStatus
_Ieee8021FrerSequenceRecoveryHandleListStatus_Object = MibTableColumn
ieee8021FrerSequenceRecoveryHandleListStatus = _Ieee8021FrerSequenceRecoveryHandleListStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 4, 4, 1, 3),
    _Ieee8021FrerSequenceRecoveryHandleListStatus_Type()
)
ieee8021FrerSequenceRecoveryHandleListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryHandleListStatus.setStatus("current")
_Ieee8021FrerSequenceRecoveryPortHandleList_ObjectIdentity = ObjectIdentity
ieee8021FrerSequenceRecoveryPortHandleList = _Ieee8021FrerSequenceRecoveryPortHandleList_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 5)
)
_Ieee8021FrerSequenceRecoveryPortHandleListTable_Object = MibTable
ieee8021FrerSequenceRecoveryPortHandleListTable = _Ieee8021FrerSequenceRecoveryPortHandleListTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 5, 5)
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryPortHandleListTable.setStatus("current")
_Ieee8021FrerSequenceRecoveryPortHandleListEntry_Object = MibTableRow
ieee8021FrerSequenceRecoveryPortHandleListEntry = _Ieee8021FrerSequenceRecoveryPortHandleListEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 5, 5, 1)
)
ieee8021FrerSequenceRecoveryPortHandleListEntry.setIndexNames(
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryIndex"),
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryPortHandleListIndex"),
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryPortHandleListEntry.setStatus("current")
_Ieee8021FrerSequenceRecoveryPortHandleListIndex_Type = Unsigned32
_Ieee8021FrerSequenceRecoveryPortHandleListIndex_Object = MibTableColumn
ieee8021FrerSequenceRecoveryPortHandleListIndex = _Ieee8021FrerSequenceRecoveryPortHandleListIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 5, 5, 1, 1),
    _Ieee8021FrerSequenceRecoveryPortHandleListIndex_Type()
)
ieee8021FrerSequenceRecoveryPortHandleListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryPortHandleListIndex.setStatus("current")
_Ieee8021FrerSequenceRecoveryPortHandle_Type = VariablePointer
_Ieee8021FrerSequenceRecoveryPortHandle_Object = MibTableColumn
ieee8021FrerSequenceRecoveryPortHandle = _Ieee8021FrerSequenceRecoveryPortHandle_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 5, 5, 1, 2),
    _Ieee8021FrerSequenceRecoveryPortHandle_Type()
)
ieee8021FrerSequenceRecoveryPortHandle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryPortHandle.setStatus("current")
_Ieee8021FrerSequenceRecoveryPortHandleListStatus_Type = RowStatus
_Ieee8021FrerSequenceRecoveryPortHandleListStatus_Object = MibTableColumn
ieee8021FrerSequenceRecoveryPortHandleListStatus = _Ieee8021FrerSequenceRecoveryPortHandleListStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 5, 5, 1, 3),
    _Ieee8021FrerSequenceRecoveryPortHandleListStatus_Type()
)
ieee8021FrerSequenceRecoveryPortHandleListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryPortHandleListStatus.setStatus("current")
_Ieee8021FrerSequenceIdentification_ObjectIdentity = ObjectIdentity
ieee8021FrerSequenceIdentification = _Ieee8021FrerSequenceIdentification_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 6)
)
_Ieee8021FrerSequenceIdentificationTable_Object = MibTable
ieee8021FrerSequenceIdentificationTable = _Ieee8021FrerSequenceIdentificationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 6, 6)
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceIdentificationTable.setStatus("current")
_Ieee8021FrerSequenceIdentificationEntry_Object = MibTableRow
ieee8021FrerSequenceIdentificationEntry = _Ieee8021FrerSequenceIdentificationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 6, 6, 1)
)
ieee8021FrerSequenceIdentificationEntry.setIndexNames(
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceIdentificationEncodePort"),
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceIdentificationEncodeDirection"),
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceIdentificationEntry.setStatus("current")
_Ieee8021FrerSequenceIdentificationEncodePort_Type = InterfaceIndex
_Ieee8021FrerSequenceIdentificationEncodePort_Object = MibTableColumn
ieee8021FrerSequenceIdentificationEncodePort = _Ieee8021FrerSequenceIdentificationEncodePort_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 6, 6, 1, 1),
    _Ieee8021FrerSequenceIdentificationEncodePort_Type()
)
ieee8021FrerSequenceIdentificationEncodePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceIdentificationEncodePort.setStatus("current")
_Ieee8021FrerSequenceIdentificationEncodeDirection_Type = TruthValue
_Ieee8021FrerSequenceIdentificationEncodeDirection_Object = MibTableColumn
ieee8021FrerSequenceIdentificationEncodeDirection = _Ieee8021FrerSequenceIdentificationEncodeDirection_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 6, 6, 1, 2),
    _Ieee8021FrerSequenceIdentificationEncodeDirection_Type()
)
ieee8021FrerSequenceIdentificationEncodeDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceIdentificationEncodeDirection.setStatus("current")
_Ieee8021FrerSequenceIdentificationStreamList_Type = AutonomousType
_Ieee8021FrerSequenceIdentificationStreamList_Object = MibTableColumn
ieee8021FrerSequenceIdentificationStreamList = _Ieee8021FrerSequenceIdentificationStreamList_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 6, 6, 1, 3),
    _Ieee8021FrerSequenceIdentificationStreamList_Type()
)
ieee8021FrerSequenceIdentificationStreamList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceIdentificationStreamList.setStatus("current")
_Ieee8021FrerSequenceIdentificationEncodeActive_Type = TruthValue
_Ieee8021FrerSequenceIdentificationEncodeActive_Object = MibTableColumn
ieee8021FrerSequenceIdentificationEncodeActive = _Ieee8021FrerSequenceIdentificationEncodeActive_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 6, 6, 1, 4),
    _Ieee8021FrerSequenceIdentificationEncodeActive_Type()
)
ieee8021FrerSequenceIdentificationEncodeActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceIdentificationEncodeActive.setStatus("current")
_Ieee8021FrerSequenceIdentificationEncodeEncapsulationType_Type = Ieee8021CBSequenceEncodeDecodeType
_Ieee8021FrerSequenceIdentificationEncodeEncapsulationType_Object = MibTableColumn
ieee8021FrerSequenceIdentificationEncodeEncapsulationType = _Ieee8021FrerSequenceIdentificationEncodeEncapsulationType_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 6, 6, 1, 5),
    _Ieee8021FrerSequenceIdentificationEncodeEncapsulationType_Type()
)
ieee8021FrerSequenceIdentificationEncodeEncapsulationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceIdentificationEncodeEncapsulationType.setStatus("current")


class _Ieee8021FrerSequenceIdentificationEncodeEncapsulationOUI_Type(OctetString):
    """Custom type ieee8021FrerSequenceIdentificationEncodeEncapsulationOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_Ieee8021FrerSequenceIdentificationEncodeEncapsulationOUI_Type.__name__ = "OctetString"
_Ieee8021FrerSequenceIdentificationEncodeEncapsulationOUI_Object = MibTableColumn
ieee8021FrerSequenceIdentificationEncodeEncapsulationOUI = _Ieee8021FrerSequenceIdentificationEncodeEncapsulationOUI_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 6, 6, 1, 6),
    _Ieee8021FrerSequenceIdentificationEncodeEncapsulationOUI_Type()
)
ieee8021FrerSequenceIdentificationEncodeEncapsulationOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceIdentificationEncodeEncapsulationOUI.setStatus("current")


class _Ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationType_Type(Integer32):
    """Custom type ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2147483647),
    )


_Ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationType_Type.__name__ = "Integer32"
_Ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationType_Object = MibTableColumn
ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationType = _Ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationType_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 6, 6, 1, 7),
    _Ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationType_Type()
)
ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationType.setStatus("current")


class _Ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationOUI_Type(OctetString):
    """Custom type ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_Ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationOUI_Type.__name__ = "OctetString"
_Ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationOUI_Object = MibTableColumn
ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationOUI = _Ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationOUI_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 6, 6, 1, 8),
    _Ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationOUI_Type()
)
ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationOUI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationOUI.setStatus("current")


class _Ieee8021FrerSequenceIdentificationEncodePathIdLanId_Type(Integer32):
    """Custom type ieee8021FrerSequenceIdentificationEncodePathIdLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Ieee8021FrerSequenceIdentificationEncodePathIdLanId_Type.__name__ = "Integer32"
_Ieee8021FrerSequenceIdentificationEncodePathIdLanId_Object = MibTableColumn
ieee8021FrerSequenceIdentificationEncodePathIdLanId = _Ieee8021FrerSequenceIdentificationEncodePathIdLanId_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 6, 6, 1, 9),
    _Ieee8021FrerSequenceIdentificationEncodePathIdLanId_Type()
)
ieee8021FrerSequenceIdentificationEncodePathIdLanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceIdentificationEncodePathIdLanId.setStatus("current")
_Ieee8021FrerSequenceIdentificationStatus_Type = RowStatus
_Ieee8021FrerSequenceIdentificationStatus_Object = MibTableColumn
ieee8021FrerSequenceIdentificationStatus = _Ieee8021FrerSequenceIdentificationStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 6, 6, 1, 10),
    _Ieee8021FrerSequenceIdentificationStatus_Type()
)
ieee8021FrerSequenceIdentificationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceIdentificationStatus.setStatus("current")
_Ieee8021FrerSequenceIdentificationHandleList_ObjectIdentity = ObjectIdentity
ieee8021FrerSequenceIdentificationHandleList = _Ieee8021FrerSequenceIdentificationHandleList_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 7)
)
_Ieee8021FrerSequenceIdentificationHandleListTable_Object = MibTable
ieee8021FrerSequenceIdentificationHandleListTable = _Ieee8021FrerSequenceIdentificationHandleListTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 7, 7)
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceIdentificationHandleListTable.setStatus("current")
_Ieee8021FrerSequenceIdentificationHandleListEntry_Object = MibTableRow
ieee8021FrerSequenceIdentificationHandleListEntry = _Ieee8021FrerSequenceIdentificationHandleListEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 7, 7, 1)
)
ieee8021FrerSequenceIdentificationHandleListEntry.setIndexNames(
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceIdentificationEncodePort"),
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceIdentificationEncodeDirection"),
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceIdentificationHandleListIndex"),
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceIdentificationHandleListEntry.setStatus("current")
_Ieee8021FrerSequenceIdentificationHandleListIndex_Type = Unsigned32
_Ieee8021FrerSequenceIdentificationHandleListIndex_Object = MibTableColumn
ieee8021FrerSequenceIdentificationHandleListIndex = _Ieee8021FrerSequenceIdentificationHandleListIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 7, 7, 1, 1),
    _Ieee8021FrerSequenceIdentificationHandleListIndex_Type()
)
ieee8021FrerSequenceIdentificationHandleListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceIdentificationHandleListIndex.setStatus("current")
_Ieee8021FrerSequenceIdentificationStreamHandle_Type = VariablePointer
_Ieee8021FrerSequenceIdentificationStreamHandle_Object = MibTableColumn
ieee8021FrerSequenceIdentificationStreamHandle = _Ieee8021FrerSequenceIdentificationStreamHandle_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 7, 7, 1, 2),
    _Ieee8021FrerSequenceIdentificationStreamHandle_Type()
)
ieee8021FrerSequenceIdentificationStreamHandle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceIdentificationStreamHandle.setStatus("current")
_Ieee8021FrerSequenceIdentificationHandleListStatus_Type = RowStatus
_Ieee8021FrerSequenceIdentificationHandleListStatus_Object = MibTableColumn
ieee8021FrerSequenceIdentificationHandleListStatus = _Ieee8021FrerSequenceIdentificationHandleListStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 7, 7, 1, 3),
    _Ieee8021FrerSequenceIdentificationHandleListStatus_Type()
)
ieee8021FrerSequenceIdentificationHandleListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceIdentificationHandleListStatus.setStatus("current")
_Ieee8021FrerStreamSplit_ObjectIdentity = ObjectIdentity
ieee8021FrerStreamSplit = _Ieee8021FrerStreamSplit_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 8)
)
_Ieee8021FrerStreamSplitTable_Object = MibTable
ieee8021FrerStreamSplitTable = _Ieee8021FrerStreamSplitTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 8, 8)
)
if mibBuilder.loadTexts:
    ieee8021FrerStreamSplitTable.setStatus("current")
_Ieee8021FrerStreamSplitEntry_Object = MibTableRow
ieee8021FrerStreamSplitEntry = _Ieee8021FrerStreamSplitEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 8, 8, 1)
)
ieee8021FrerStreamSplitEntry.setIndexNames(
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerStreamSplitIndex"),
)
if mibBuilder.loadTexts:
    ieee8021FrerStreamSplitEntry.setStatus("current")
_Ieee8021FrerStreamSplitIndex_Type = Unsigned32
_Ieee8021FrerStreamSplitIndex_Object = MibTableColumn
ieee8021FrerStreamSplitIndex = _Ieee8021FrerStreamSplitIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 8, 8, 1, 1),
    _Ieee8021FrerStreamSplitIndex_Type()
)
ieee8021FrerStreamSplitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FrerStreamSplitIndex.setStatus("current")
_Ieee8021FrerStreamSplitPort_Type = InterfaceIndex
_Ieee8021FrerStreamSplitPort_Object = MibTableColumn
ieee8021FrerStreamSplitPort = _Ieee8021FrerStreamSplitPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 8, 8, 1, 2),
    _Ieee8021FrerStreamSplitPort_Type()
)
ieee8021FrerStreamSplitPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerStreamSplitPort.setStatus("current")
_Ieee8021FrerStreamSplitDirection_Type = TruthValue
_Ieee8021FrerStreamSplitDirection_Object = MibTableColumn
ieee8021FrerStreamSplitDirection = _Ieee8021FrerStreamSplitDirection_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 8, 8, 1, 3),
    _Ieee8021FrerStreamSplitDirection_Type()
)
ieee8021FrerStreamSplitDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerStreamSplitDirection.setStatus("current")
_Ieee8021FrerStreamSplitInputIdList_Type = AutonomousType
_Ieee8021FrerStreamSplitInputIdList_Object = MibTableColumn
ieee8021FrerStreamSplitInputIdList = _Ieee8021FrerStreamSplitInputIdList_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 8, 8, 1, 4),
    _Ieee8021FrerStreamSplitInputIdList_Type()
)
ieee8021FrerStreamSplitInputIdList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021FrerStreamSplitInputIdList.setStatus("current")
_Ieee8021FrerStreamSplitOutputIdList_Type = AutonomousType
_Ieee8021FrerStreamSplitOutputIdList_Object = MibTableColumn
ieee8021FrerStreamSplitOutputIdList = _Ieee8021FrerStreamSplitOutputIdList_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 8, 8, 1, 5),
    _Ieee8021FrerStreamSplitOutputIdList_Type()
)
ieee8021FrerStreamSplitOutputIdList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021FrerStreamSplitOutputIdList.setStatus("current")
_Ieee8021FrerStreamSplitInputHandleList_ObjectIdentity = ObjectIdentity
ieee8021FrerStreamSplitInputHandleList = _Ieee8021FrerStreamSplitInputHandleList_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 9)
)
_Ieee8021FrerStreamSplitInputHandleListTable_Object = MibTable
ieee8021FrerStreamSplitInputHandleListTable = _Ieee8021FrerStreamSplitInputHandleListTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 9, 9)
)
if mibBuilder.loadTexts:
    ieee8021FrerStreamSplitInputHandleListTable.setStatus("current")
_Ieee8021FrerStreamSplitInputHandleListEntry_Object = MibTableRow
ieee8021FrerStreamSplitInputHandleListEntry = _Ieee8021FrerStreamSplitInputHandleListEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 9, 9, 1)
)
ieee8021FrerStreamSplitInputHandleListEntry.setIndexNames(
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerStreamSplitIndex"),
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerStreamSplitInputHandleListIndex"),
)
if mibBuilder.loadTexts:
    ieee8021FrerStreamSplitInputHandleListEntry.setStatus("current")
_Ieee8021FrerStreamSplitInputHandleListIndex_Type = Unsigned32
_Ieee8021FrerStreamSplitInputHandleListIndex_Object = MibTableColumn
ieee8021FrerStreamSplitInputHandleListIndex = _Ieee8021FrerStreamSplitInputHandleListIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 9, 9, 1, 1),
    _Ieee8021FrerStreamSplitInputHandleListIndex_Type()
)
ieee8021FrerStreamSplitInputHandleListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FrerStreamSplitInputHandleListIndex.setStatus("current")
_Ieee8021FrerStreamSplitInputIdHandle_Type = VariablePointer
_Ieee8021FrerStreamSplitInputIdHandle_Object = MibTableColumn
ieee8021FrerStreamSplitInputIdHandle = _Ieee8021FrerStreamSplitInputIdHandle_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 9, 9, 1, 2),
    _Ieee8021FrerStreamSplitInputIdHandle_Type()
)
ieee8021FrerStreamSplitInputIdHandle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerStreamSplitInputIdHandle.setStatus("current")
_Ieee8021FrerStreamSplitInputHandleListStatus_Type = RowStatus
_Ieee8021FrerStreamSplitInputHandleListStatus_Object = MibTableColumn
ieee8021FrerStreamSplitInputHandleListStatus = _Ieee8021FrerStreamSplitInputHandleListStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 9, 9, 1, 3),
    _Ieee8021FrerStreamSplitInputHandleListStatus_Type()
)
ieee8021FrerStreamSplitInputHandleListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerStreamSplitInputHandleListStatus.setStatus("current")
_Ieee8021FrerStreamSplitOutputHandleList_ObjectIdentity = ObjectIdentity
ieee8021FrerStreamSplitOutputHandleList = _Ieee8021FrerStreamSplitOutputHandleList_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 10)
)
_Ieee8021FrerStreamSplitOutputHandleListTable_Object = MibTable
ieee8021FrerStreamSplitOutputHandleListTable = _Ieee8021FrerStreamSplitOutputHandleListTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 10, 10)
)
if mibBuilder.loadTexts:
    ieee8021FrerStreamSplitOutputHandleListTable.setStatus("current")
_Ieee8021FrerStreamSplitOutputHandleListEntry_Object = MibTableRow
ieee8021FrerStreamSplitOutputHandleListEntry = _Ieee8021FrerStreamSplitOutputHandleListEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 10, 10, 1)
)
ieee8021FrerStreamSplitOutputHandleListEntry.setIndexNames(
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerStreamSplitIndex"),
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerStreamSplitOutputHandleListIndex"),
)
if mibBuilder.loadTexts:
    ieee8021FrerStreamSplitOutputHandleListEntry.setStatus("current")
_Ieee8021FrerStreamSplitOutputHandleListIndex_Type = Unsigned32
_Ieee8021FrerStreamSplitOutputHandleListIndex_Object = MibTableColumn
ieee8021FrerStreamSplitOutputHandleListIndex = _Ieee8021FrerStreamSplitOutputHandleListIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 10, 10, 1, 1),
    _Ieee8021FrerStreamSplitOutputHandleListIndex_Type()
)
ieee8021FrerStreamSplitOutputHandleListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FrerStreamSplitOutputHandleListIndex.setStatus("current")
_Ieee8021FrerStreamSplitOutputIdHandle_Type = VariablePointer
_Ieee8021FrerStreamSplitOutputIdHandle_Object = MibTableColumn
ieee8021FrerStreamSplitOutputIdHandle = _Ieee8021FrerStreamSplitOutputIdHandle_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 10, 10, 1, 2),
    _Ieee8021FrerStreamSplitOutputIdHandle_Type()
)
ieee8021FrerStreamSplitOutputIdHandle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerStreamSplitOutputIdHandle.setStatus("current")
_Ieee8021FrerStreamSplitOutputHandleListStatus_Type = RowStatus
_Ieee8021FrerStreamSplitOutputHandleListStatus_Object = MibTableColumn
ieee8021FrerStreamSplitOutputHandleListStatus = _Ieee8021FrerStreamSplitOutputHandleListStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 10, 10, 1, 3),
    _Ieee8021FrerStreamSplitOutputHandleListStatus_Type()
)
ieee8021FrerStreamSplitOutputHandleListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerStreamSplitOutputHandleListStatus.setStatus("current")
_Ieee8021FrerSequenceAutoconfig_ObjectIdentity = ObjectIdentity
ieee8021FrerSequenceAutoconfig = _Ieee8021FrerSequenceAutoconfig_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11)
)
_Ieee8021FrerSequenceAutoconfigTable_Object = MibTable
ieee8021FrerSequenceAutoconfigTable = _Ieee8021FrerSequenceAutoconfigTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11)
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigTable.setStatus("current")
_Ieee8021FrerSequenceAutoconfigEntry_Object = MibTableRow
ieee8021FrerSequenceAutoconfigEntry = _Ieee8021FrerSequenceAutoconfigEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1)
)
ieee8021FrerSequenceAutoconfigEntry.setIndexNames(
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigIndex"),
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigEntry.setStatus("current")
_Ieee8021FrerSequenceAutoconfigIndex_Type = Unsigned32
_Ieee8021FrerSequenceAutoconfigIndex_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigIndex = _Ieee8021FrerSequenceAutoconfigIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 1),
    _Ieee8021FrerSequenceAutoconfigIndex_Type()
)
ieee8021FrerSequenceAutoconfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigIndex.setStatus("current")
_Ieee8021FrerSequenceAutoconfigSequenceEncapsulation_Type = Ieee8021CBSequenceEncodeDecodeType
_Ieee8021FrerSequenceAutoconfigSequenceEncapsulation_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigSequenceEncapsulation = _Ieee8021FrerSequenceAutoconfigSequenceEncapsulation_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 2),
    _Ieee8021FrerSequenceAutoconfigSequenceEncapsulation_Type()
)
ieee8021FrerSequenceAutoconfigSequenceEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigSequenceEncapsulation.setStatus("current")


class _Ieee8021FrerSequenceAutoconfigSequenceEncapsulationOUI_Type(OctetString):
    """Custom type ieee8021FrerSequenceAutoconfigSequenceEncapsulationOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_Ieee8021FrerSequenceAutoconfigSequenceEncapsulationOUI_Type.__name__ = "OctetString"
_Ieee8021FrerSequenceAutoconfigSequenceEncapsulationOUI_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigSequenceEncapsulationOUI = _Ieee8021FrerSequenceAutoconfigSequenceEncapsulationOUI_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 3),
    _Ieee8021FrerSequenceAutoconfigSequenceEncapsulationOUI_Type()
)
ieee8021FrerSequenceAutoconfigSequenceEncapsulationOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigSequenceEncapsulationOUI.setStatus("current")


class _Ieee8021FrerSequenceAutoconfigCustomSequenceEncapsulation_Type(Integer32):
    """Custom type ieee8021FrerSequenceAutoconfigCustomSequenceEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2147483647),
    )


_Ieee8021FrerSequenceAutoconfigCustomSequenceEncapsulation_Type.__name__ = "Integer32"
_Ieee8021FrerSequenceAutoconfigCustomSequenceEncapsulation_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigCustomSequenceEncapsulation = _Ieee8021FrerSequenceAutoconfigCustomSequenceEncapsulation_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 4),
    _Ieee8021FrerSequenceAutoconfigCustomSequenceEncapsulation_Type()
)
ieee8021FrerSequenceAutoconfigCustomSequenceEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigCustomSequenceEncapsulation.setStatus("current")


class _Ieee8021FrerSequenceAutoconfigCustomSequenceEncOUI_Type(OctetString):
    """Custom type ieee8021FrerSequenceAutoconfigCustomSequenceEncOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_Ieee8021FrerSequenceAutoconfigCustomSequenceEncOUI_Type.__name__ = "OctetString"
_Ieee8021FrerSequenceAutoconfigCustomSequenceEncOUI_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigCustomSequenceEncOUI = _Ieee8021FrerSequenceAutoconfigCustomSequenceEncOUI_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 5),
    _Ieee8021FrerSequenceAutoconfigCustomSequenceEncOUI_Type()
)
ieee8021FrerSequenceAutoconfigCustomSequenceEncOUI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigCustomSequenceEncOUI.setStatus("current")
_Ieee8021FrerSequenceAutoconfigReceivePortList_Type = AutonomousType
_Ieee8021FrerSequenceAutoconfigReceivePortList_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigReceivePortList = _Ieee8021FrerSequenceAutoconfigReceivePortList_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 6),
    _Ieee8021FrerSequenceAutoconfigReceivePortList_Type()
)
ieee8021FrerSequenceAutoconfigReceivePortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigReceivePortList.setStatus("current")
_Ieee8021FrerSequenceAutoconfigTagged_Type = Ieee8021CBTaggedType
_Ieee8021FrerSequenceAutoconfigTagged_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigTagged = _Ieee8021FrerSequenceAutoconfigTagged_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 7),
    _Ieee8021FrerSequenceAutoconfigTagged_Type()
)
ieee8021FrerSequenceAutoconfigTagged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigTagged.setStatus("current")
_Ieee8021FrerSequenceAutoconfigVlanList_Type = AutonomousType
_Ieee8021FrerSequenceAutoconfigVlanList_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigVlanList = _Ieee8021FrerSequenceAutoconfigVlanList_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 8),
    _Ieee8021FrerSequenceAutoconfigVlanList_Type()
)
ieee8021FrerSequenceAutoconfigVlanList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigVlanList.setStatus("current")
_Ieee8021FrerSequenceAutoconfigRecoveryPortList_Type = AutonomousType
_Ieee8021FrerSequenceAutoconfigRecoveryPortList_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigRecoveryPortList = _Ieee8021FrerSequenceAutoconfigRecoveryPortList_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 9),
    _Ieee8021FrerSequenceAutoconfigRecoveryPortList_Type()
)
ieee8021FrerSequenceAutoconfigRecoveryPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigRecoveryPortList.setStatus("current")


class _Ieee8021FrerSequenceAutoconfigDestructMSec_Type(Integer32):
    """Custom type ieee8021FrerSequenceAutoconfigDestructMSec based on Integer32"""
    defaultValue = 86400000


_Ieee8021FrerSequenceAutoconfigDestructMSec_Type.__name__ = "Integer32"
_Ieee8021FrerSequenceAutoconfigDestructMSec_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigDestructMSec = _Ieee8021FrerSequenceAutoconfigDestructMSec_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 10),
    _Ieee8021FrerSequenceAutoconfigDestructMSec_Type()
)
ieee8021FrerSequenceAutoconfigDestructMSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigDestructMSec.setStatus("current")
_Ieee8021FrerSequenceAutoconfigResetMSec_Type = Unsigned32
_Ieee8021FrerSequenceAutoconfigResetMSec_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigResetMSec = _Ieee8021FrerSequenceAutoconfigResetMSec_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 11),
    _Ieee8021FrerSequenceAutoconfigResetMSec_Type()
)
ieee8021FrerSequenceAutoconfigResetMSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigResetMSec.setStatus("current")
_Ieee8021FrerSequenceAutoconfigAlgorithm_Type = Ieee8021CBSequenceRecoveryAlgorithm
_Ieee8021FrerSequenceAutoconfigAlgorithm_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigAlgorithm = _Ieee8021FrerSequenceAutoconfigAlgorithm_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 12),
    _Ieee8021FrerSequenceAutoconfigAlgorithm_Type()
)
ieee8021FrerSequenceAutoconfigAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigAlgorithm.setStatus("current")


class _Ieee8021FrerSequenceAutoconfigAlgorithmOUI_Type(OctetString):
    """Custom type ieee8021FrerSequenceAutoconfigAlgorithmOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_Ieee8021FrerSequenceAutoconfigAlgorithmOUI_Type.__name__ = "OctetString"
_Ieee8021FrerSequenceAutoconfigAlgorithmOUI_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigAlgorithmOUI = _Ieee8021FrerSequenceAutoconfigAlgorithmOUI_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 13),
    _Ieee8021FrerSequenceAutoconfigAlgorithmOUI_Type()
)
ieee8021FrerSequenceAutoconfigAlgorithmOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigAlgorithmOUI.setStatus("current")


class _Ieee8021FrerSequenceAutoconfigCustomAlgorithm_Type(Integer32):
    """Custom type ieee8021FrerSequenceAutoconfigCustomAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2147483647),
    )


_Ieee8021FrerSequenceAutoconfigCustomAlgorithm_Type.__name__ = "Integer32"
_Ieee8021FrerSequenceAutoconfigCustomAlgorithm_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigCustomAlgorithm = _Ieee8021FrerSequenceAutoconfigCustomAlgorithm_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 14),
    _Ieee8021FrerSequenceAutoconfigCustomAlgorithm_Type()
)
ieee8021FrerSequenceAutoconfigCustomAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigCustomAlgorithm.setStatus("current")


class _Ieee8021FrerSequenceAutoconfigCustomAlgorithmOUI_Type(OctetString):
    """Custom type ieee8021FrerSequenceAutoconfigCustomAlgorithmOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_Ieee8021FrerSequenceAutoconfigCustomAlgorithmOUI_Type.__name__ = "OctetString"
_Ieee8021FrerSequenceAutoconfigCustomAlgorithmOUI_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigCustomAlgorithmOUI = _Ieee8021FrerSequenceAutoconfigCustomAlgorithmOUI_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 15),
    _Ieee8021FrerSequenceAutoconfigCustomAlgorithmOUI_Type()
)
ieee8021FrerSequenceAutoconfigCustomAlgorithmOUI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigCustomAlgorithmOUI.setStatus("current")
_Ieee8021FrerSequenceAutoconfigHistoryLength_Type = Integer32
_Ieee8021FrerSequenceAutoconfigHistoryLength_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigHistoryLength = _Ieee8021FrerSequenceAutoconfigHistoryLength_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 16),
    _Ieee8021FrerSequenceAutoconfigHistoryLength_Type()
)
ieee8021FrerSequenceAutoconfigHistoryLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigHistoryLength.setStatus("current")
_Ieee8021FrerSequenceAutoconfigCreateIndividual_Type = TruthValue
_Ieee8021FrerSequenceAutoconfigCreateIndividual_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigCreateIndividual = _Ieee8021FrerSequenceAutoconfigCreateIndividual_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 17),
    _Ieee8021FrerSequenceAutoconfigCreateIndividual_Type()
)
ieee8021FrerSequenceAutoconfigCreateIndividual.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigCreateIndividual.setStatus("current")
_Ieee8021FrerSequenceAutoconfigCreateRecovery_Type = TruthValue
_Ieee8021FrerSequenceAutoconfigCreateRecovery_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigCreateRecovery = _Ieee8021FrerSequenceAutoconfigCreateRecovery_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 18),
    _Ieee8021FrerSequenceAutoconfigCreateRecovery_Type()
)
ieee8021FrerSequenceAutoconfigCreateRecovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigCreateRecovery.setStatus("current")
_Ieee8021FrerSequenceAutoconfigLatentErrorDetection_Type = TruthValue
_Ieee8021FrerSequenceAutoconfigLatentErrorDetection_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigLatentErrorDetection = _Ieee8021FrerSequenceAutoconfigLatentErrorDetection_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 19),
    _Ieee8021FrerSequenceAutoconfigLatentErrorDetection_Type()
)
ieee8021FrerSequenceAutoconfigLatentErrorDetection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigLatentErrorDetection.setStatus("current")
_Ieee8021FrerSequenceAutoconfigLatentErrorDifference_Type = Integer32
_Ieee8021FrerSequenceAutoconfigLatentErrorDifference_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigLatentErrorDifference = _Ieee8021FrerSequenceAutoconfigLatentErrorDifference_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 20),
    _Ieee8021FrerSequenceAutoconfigLatentErrorDifference_Type()
)
ieee8021FrerSequenceAutoconfigLatentErrorDifference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigLatentErrorDifference.setStatus("current")
_Ieee8021FrerSequenceAutoconfigLatentErrorPeriod_Type = Integer32
_Ieee8021FrerSequenceAutoconfigLatentErrorPeriod_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigLatentErrorPeriod = _Ieee8021FrerSequenceAutoconfigLatentErrorPeriod_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 21),
    _Ieee8021FrerSequenceAutoconfigLatentErrorPeriod_Type()
)
ieee8021FrerSequenceAutoconfigLatentErrorPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigLatentErrorPeriod.setStatus("current")
_Ieee8021FrerSequenceAutoconfigLatentErrorResetPeriod_Type = Integer32
_Ieee8021FrerSequenceAutoconfigLatentErrorResetPeriod_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigLatentErrorResetPeriod = _Ieee8021FrerSequenceAutoconfigLatentErrorResetPeriod_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 22),
    _Ieee8021FrerSequenceAutoconfigLatentErrorResetPeriod_Type()
)
ieee8021FrerSequenceAutoconfigLatentErrorResetPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigLatentErrorResetPeriod.setStatus("current")
_Ieee8021FrerSequenceAutoconfigStatus_Type = RowStatus
_Ieee8021FrerSequenceAutoconfigStatus_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigStatus = _Ieee8021FrerSequenceAutoconfigStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 11, 11, 1, 23),
    _Ieee8021FrerSequenceAutoconfigStatus_Type()
)
ieee8021FrerSequenceAutoconfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigStatus.setStatus("current")
_Ieee8021FrerSequenceAutoconfigReceivePortHandleList_ObjectIdentity = ObjectIdentity
ieee8021FrerSequenceAutoconfigReceivePortHandleList = _Ieee8021FrerSequenceAutoconfigReceivePortHandleList_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 12)
)
_Ieee8021FrerSequenceAutoconfigReceivePortHandleListTable_Object = MibTable
ieee8021FrerSequenceAutoconfigReceivePortHandleListTable = _Ieee8021FrerSequenceAutoconfigReceivePortHandleListTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 12, 12)
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigReceivePortHandleListTable.setStatus("current")
_Ieee8021FrerSequenceAutoconfigReceivePortHandleListEntry_Object = MibTableRow
ieee8021FrerSequenceAutoconfigReceivePortHandleListEntry = _Ieee8021FrerSequenceAutoconfigReceivePortHandleListEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 12, 12, 1)
)
ieee8021FrerSequenceAutoconfigReceivePortHandleListEntry.setIndexNames(
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigIndex"),
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigReceivePortHandleListIndex"),
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigReceivePortHandleListEntry.setStatus("current")
_Ieee8021FrerSequenceAutoconfigReceivePortHandleListIndex_Type = Unsigned32
_Ieee8021FrerSequenceAutoconfigReceivePortHandleListIndex_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigReceivePortHandleListIndex = _Ieee8021FrerSequenceAutoconfigReceivePortHandleListIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 12, 12, 1, 1),
    _Ieee8021FrerSequenceAutoconfigReceivePortHandleListIndex_Type()
)
ieee8021FrerSequenceAutoconfigReceivePortHandleListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigReceivePortHandleListIndex.setStatus("current")
_Ieee8021FrerSequenceAutoconfigReceivePortHandle_Type = VariablePointer
_Ieee8021FrerSequenceAutoconfigReceivePortHandle_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigReceivePortHandle = _Ieee8021FrerSequenceAutoconfigReceivePortHandle_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 12, 12, 1, 2),
    _Ieee8021FrerSequenceAutoconfigReceivePortHandle_Type()
)
ieee8021FrerSequenceAutoconfigReceivePortHandle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigReceivePortHandle.setStatus("current")
_Ieee8021FrerSequenceAutoconfigReceivePortHandleListStatus_Type = RowStatus
_Ieee8021FrerSequenceAutoconfigReceivePortHandleListStatus_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigReceivePortHandleListStatus = _Ieee8021FrerSequenceAutoconfigReceivePortHandleListStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 12, 12, 1, 3),
    _Ieee8021FrerSequenceAutoconfigReceivePortHandleListStatus_Type()
)
ieee8021FrerSequenceAutoconfigReceivePortHandleListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigReceivePortHandleListStatus.setStatus("current")
_Ieee8021FrerSequenceAutoconfigVlanHandleList_ObjectIdentity = ObjectIdentity
ieee8021FrerSequenceAutoconfigVlanHandleList = _Ieee8021FrerSequenceAutoconfigVlanHandleList_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 13)
)
_Ieee8021FrerSequenceAutoconfigVlanListTable_Object = MibTable
ieee8021FrerSequenceAutoconfigVlanListTable = _Ieee8021FrerSequenceAutoconfigVlanListTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 13, 13)
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigVlanListTable.setStatus("current")
_Ieee8021FrerSequenceAutoconfigVlanListEntry_Object = MibTableRow
ieee8021FrerSequenceAutoconfigVlanListEntry = _Ieee8021FrerSequenceAutoconfigVlanListEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 13, 13, 1)
)
ieee8021FrerSequenceAutoconfigVlanListEntry.setIndexNames(
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigIndex"),
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigVlanListIndex"),
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigVlanListEntry.setStatus("current")
_Ieee8021FrerSequenceAutoconfigVlanListIndex_Type = Unsigned32
_Ieee8021FrerSequenceAutoconfigVlanListIndex_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigVlanListIndex = _Ieee8021FrerSequenceAutoconfigVlanListIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 13, 13, 1, 1),
    _Ieee8021FrerSequenceAutoconfigVlanListIndex_Type()
)
ieee8021FrerSequenceAutoconfigVlanListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigVlanListIndex.setStatus("current")
_Ieee8021FrerSequenceAutoconfigVlan_Type = Ieee8021CBVlanIdentifier
_Ieee8021FrerSequenceAutoconfigVlan_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigVlan = _Ieee8021FrerSequenceAutoconfigVlan_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 13, 13, 1, 2),
    _Ieee8021FrerSequenceAutoconfigVlan_Type()
)
ieee8021FrerSequenceAutoconfigVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigVlan.setStatus("current")
_Ieee8021FrerSequenceAutoconfigVlanListStatus_Type = RowStatus
_Ieee8021FrerSequenceAutoconfigVlanListStatus_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigVlanListStatus = _Ieee8021FrerSequenceAutoconfigVlanListStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 13, 13, 1, 3),
    _Ieee8021FrerSequenceAutoconfigVlanListStatus_Type()
)
ieee8021FrerSequenceAutoconfigVlanListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigVlanListStatus.setStatus("current")
_Ieee8021FrerSequenceAutoconfigRecoveryPortHandleList_ObjectIdentity = ObjectIdentity
ieee8021FrerSequenceAutoconfigRecoveryPortHandleList = _Ieee8021FrerSequenceAutoconfigRecoveryPortHandleList_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 14)
)
_Ieee8021FrerSequenceAutoconfigRecoveryPortHandleListTable_Object = MibTable
ieee8021FrerSequenceAutoconfigRecoveryPortHandleListTable = _Ieee8021FrerSequenceAutoconfigRecoveryPortHandleListTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 14, 14)
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigRecoveryPortHandleListTable.setStatus("current")
_Ieee8021FrerSequenceAutoconfigRecoveryPortHandleListEntry_Object = MibTableRow
ieee8021FrerSequenceAutoconfigRecoveryPortHandleListEntry = _Ieee8021FrerSequenceAutoconfigRecoveryPortHandleListEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 14, 14, 1)
)
ieee8021FrerSequenceAutoconfigRecoveryPortHandleListEntry.setIndexNames(
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigIndex"),
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigRecoveryPortHandleListIndex"),
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigRecoveryPortHandleListEntry.setStatus("current")
_Ieee8021FrerSequenceAutoconfigRecoveryPortHandleListIndex_Type = Unsigned32
_Ieee8021FrerSequenceAutoconfigRecoveryPortHandleListIndex_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigRecoveryPortHandleListIndex = _Ieee8021FrerSequenceAutoconfigRecoveryPortHandleListIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 14, 14, 1, 1),
    _Ieee8021FrerSequenceAutoconfigRecoveryPortHandleListIndex_Type()
)
ieee8021FrerSequenceAutoconfigRecoveryPortHandleListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigRecoveryPortHandleListIndex.setStatus("current")
_Ieee8021FrerSequenceAutoconfigRecoveryPortHandle_Type = VariablePointer
_Ieee8021FrerSequenceAutoconfigRecoveryPortHandle_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigRecoveryPortHandle = _Ieee8021FrerSequenceAutoconfigRecoveryPortHandle_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 14, 14, 1, 2),
    _Ieee8021FrerSequenceAutoconfigRecoveryPortHandle_Type()
)
ieee8021FrerSequenceAutoconfigRecoveryPortHandle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigRecoveryPortHandle.setStatus("current")
_Ieee8021FrerSequenceAutoconfigRecoveryPortHandleListStatus_Type = RowStatus
_Ieee8021FrerSequenceAutoconfigRecoveryPortHandleListStatus_Object = MibTableColumn
ieee8021FrerSequenceAutoconfigRecoveryPortHandleListStatus = _Ieee8021FrerSequenceAutoconfigRecoveryPortHandleListStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 14, 14, 1, 3),
    _Ieee8021FrerSequenceAutoconfigRecoveryPortHandleListStatus_Type()
)
ieee8021FrerSequenceAutoconfigRecoveryPortHandleListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigRecoveryPortHandleListStatus.setStatus("current")
_Ieee8021FrerOutputAutoconfig_ObjectIdentity = ObjectIdentity
ieee8021FrerOutputAutoconfig = _Ieee8021FrerOutputAutoconfig_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 15)
)
_Ieee8021FrerOutputAutoconfigTable_Object = MibTable
ieee8021FrerOutputAutoconfigTable = _Ieee8021FrerOutputAutoconfigTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 15, 15)
)
if mibBuilder.loadTexts:
    ieee8021FrerOutputAutoconfigTable.setStatus("current")
_Ieee8021FrerOutputAutoconfigEntry_Object = MibTableRow
ieee8021FrerOutputAutoconfigEntry = _Ieee8021FrerOutputAutoconfigEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 15, 15, 1)
)
ieee8021FrerOutputAutoconfigEntry.setIndexNames(
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerOutputAutoconfigIndex"),
)
if mibBuilder.loadTexts:
    ieee8021FrerOutputAutoconfigEntry.setStatus("current")
_Ieee8021FrerOutputAutoconfigIndex_Type = Unsigned32
_Ieee8021FrerOutputAutoconfigIndex_Object = MibTableColumn
ieee8021FrerOutputAutoconfigIndex = _Ieee8021FrerOutputAutoconfigIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 15, 15, 1, 1),
    _Ieee8021FrerOutputAutoconfigIndex_Type()
)
ieee8021FrerOutputAutoconfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FrerOutputAutoconfigIndex.setStatus("current")
_Ieee8021FrerOutputAutoconfigPortList_Type = AutonomousType
_Ieee8021FrerOutputAutoconfigPortList_Object = MibTableColumn
ieee8021FrerOutputAutoconfigPortList = _Ieee8021FrerOutputAutoconfigPortList_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 15, 15, 1, 2),
    _Ieee8021FrerOutputAutoconfigPortList_Type()
)
ieee8021FrerOutputAutoconfigPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerOutputAutoconfigPortList.setStatus("current")
_Ieee8021FrerOutputAutoconfigEncapsulation_Type = Ieee8021CBSequenceEncodeDecodeType
_Ieee8021FrerOutputAutoconfigEncapsulation_Object = MibTableColumn
ieee8021FrerOutputAutoconfigEncapsulation = _Ieee8021FrerOutputAutoconfigEncapsulation_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 15, 15, 1, 3),
    _Ieee8021FrerOutputAutoconfigEncapsulation_Type()
)
ieee8021FrerOutputAutoconfigEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerOutputAutoconfigEncapsulation.setStatus("current")


class _Ieee8021FrerOutputAutoconfigEncapsulationOUI_Type(OctetString):
    """Custom type ieee8021FrerOutputAutoconfigEncapsulationOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_Ieee8021FrerOutputAutoconfigEncapsulationOUI_Type.__name__ = "OctetString"
_Ieee8021FrerOutputAutoconfigEncapsulationOUI_Object = MibTableColumn
ieee8021FrerOutputAutoconfigEncapsulationOUI = _Ieee8021FrerOutputAutoconfigEncapsulationOUI_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 15, 15, 1, 4),
    _Ieee8021FrerOutputAutoconfigEncapsulationOUI_Type()
)
ieee8021FrerOutputAutoconfigEncapsulationOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FrerOutputAutoconfigEncapsulationOUI.setStatus("current")


class _Ieee8021FrerOutputAutoconfigCustomEncapsulation_Type(Integer32):
    """Custom type ieee8021FrerOutputAutoconfigCustomEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2147483647),
    )


_Ieee8021FrerOutputAutoconfigCustomEncapsulation_Type.__name__ = "Integer32"
_Ieee8021FrerOutputAutoconfigCustomEncapsulation_Object = MibTableColumn
ieee8021FrerOutputAutoconfigCustomEncapsulation = _Ieee8021FrerOutputAutoconfigCustomEncapsulation_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 15, 15, 1, 5),
    _Ieee8021FrerOutputAutoconfigCustomEncapsulation_Type()
)
ieee8021FrerOutputAutoconfigCustomEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerOutputAutoconfigCustomEncapsulation.setStatus("current")


class _Ieee8021FrerOutputAutoconfigCustomEncapsulationOUI_Type(OctetString):
    """Custom type ieee8021FrerOutputAutoconfigCustomEncapsulationOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixedLength = 3


_Ieee8021FrerOutputAutoconfigCustomEncapsulationOUI_Type.__name__ = "OctetString"
_Ieee8021FrerOutputAutoconfigCustomEncapsulationOUI_Object = MibTableColumn
ieee8021FrerOutputAutoconfigCustomEncapsulationOUI = _Ieee8021FrerOutputAutoconfigCustomEncapsulationOUI_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 15, 15, 1, 6),
    _Ieee8021FrerOutputAutoconfigCustomEncapsulationOUI_Type()
)
ieee8021FrerOutputAutoconfigCustomEncapsulationOUI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerOutputAutoconfigCustomEncapsulationOUI.setStatus("current")
_Ieee8021FrerOutputAutoconfigLanPathId_Type = Ieee8021CBLanPathIdType
_Ieee8021FrerOutputAutoconfigLanPathId_Object = MibTableColumn
ieee8021FrerOutputAutoconfigLanPathId = _Ieee8021FrerOutputAutoconfigLanPathId_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 15, 15, 1, 7),
    _Ieee8021FrerOutputAutoconfigLanPathId_Type()
)
ieee8021FrerOutputAutoconfigLanPathId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerOutputAutoconfigLanPathId.setStatus("current")
_Ieee8021FrerOutputAutoconfigStatus_Type = RowStatus
_Ieee8021FrerOutputAutoconfigStatus_Object = MibTableColumn
ieee8021FrerOutputAutoconfigStatus = _Ieee8021FrerOutputAutoconfigStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 15, 15, 1, 8),
    _Ieee8021FrerOutputAutoconfigStatus_Type()
)
ieee8021FrerOutputAutoconfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerOutputAutoconfigStatus.setStatus("current")
_Ieee8021FrerOutputAutoconfigPortHandleList_ObjectIdentity = ObjectIdentity
ieee8021FrerOutputAutoconfigPortHandleList = _Ieee8021FrerOutputAutoconfigPortHandleList_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 16)
)
_Ieee8021FrerOutputAutoconfigPortHandleListTable_Object = MibTable
ieee8021FrerOutputAutoconfigPortHandleListTable = _Ieee8021FrerOutputAutoconfigPortHandleListTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 16, 16)
)
if mibBuilder.loadTexts:
    ieee8021FrerOutputAutoconfigPortHandleListTable.setStatus("current")
_Ieee8021FrerOutputAutoconfigPortHandleListEntry_Object = MibTableRow
ieee8021FrerOutputAutoconfigPortHandleListEntry = _Ieee8021FrerOutputAutoconfigPortHandleListEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 16, 16, 1)
)
ieee8021FrerOutputAutoconfigPortHandleListEntry.setIndexNames(
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerOutputAutoconfigIndex"),
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerOutputAutoconfigPortHandleListIndex"),
)
if mibBuilder.loadTexts:
    ieee8021FrerOutputAutoconfigPortHandleListEntry.setStatus("current")
_Ieee8021FrerOutputAutoconfigPortHandleListIndex_Type = Unsigned32
_Ieee8021FrerOutputAutoconfigPortHandleListIndex_Object = MibTableColumn
ieee8021FrerOutputAutoconfigPortHandleListIndex = _Ieee8021FrerOutputAutoconfigPortHandleListIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 16, 16, 1, 1),
    _Ieee8021FrerOutputAutoconfigPortHandleListIndex_Type()
)
ieee8021FrerOutputAutoconfigPortHandleListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FrerOutputAutoconfigPortHandleListIndex.setStatus("current")
_Ieee8021FrerOutputAutoconfigPortHandle_Type = VariablePointer
_Ieee8021FrerOutputAutoconfigPortHandle_Object = MibTableColumn
ieee8021FrerOutputAutoconfigPortHandle = _Ieee8021FrerOutputAutoconfigPortHandle_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 16, 16, 1, 2),
    _Ieee8021FrerOutputAutoconfigPortHandle_Type()
)
ieee8021FrerOutputAutoconfigPortHandle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerOutputAutoconfigPortHandle.setStatus("current")
_Ieee8021FrerOutputAutoconfigPortHandleListStatus_Type = RowStatus
_Ieee8021FrerOutputAutoconfigPortHandleListStatus_Object = MibTableColumn
ieee8021FrerOutputAutoconfigPortHandleListStatus = _Ieee8021FrerOutputAutoconfigPortHandleListStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 16, 16, 1, 3),
    _Ieee8021FrerOutputAutoconfigPortHandleListStatus_Type()
)
ieee8021FrerOutputAutoconfigPortHandleListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021FrerOutputAutoconfigPortHandleListStatus.setStatus("current")
_Ieee8021FrerPerPortPerStreamCounters_ObjectIdentity = ObjectIdentity
ieee8021FrerPerPortPerStreamCounters = _Ieee8021FrerPerPortPerStreamCounters_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 17)
)
_Ieee8021FrerPerPortPerStreamCountersTable_Object = MibTable
ieee8021FrerPerPortPerStreamCountersTable = _Ieee8021FrerPerPortPerStreamCountersTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 17, 17)
)
if mibBuilder.loadTexts:
    ieee8021FrerPerPortPerStreamCountersTable.setStatus("current")
_Ieee8021FrerPerPortPerStreamCountersEntry_Object = MibTableRow
ieee8021FrerPerPortPerStreamCountersEntry = _Ieee8021FrerPerPortPerStreamCountersEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 17, 17, 1)
)
ieee8021FrerPerPortPerStreamCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE8021-STREAM-IDENTIFICATION-MIB", "ieee8021StreamIdStreamIdHandle"),
    (0, "IEEE8021-FRER-MIB", "ieee8021FrerPerPortPerStreamDirection"),
)
if mibBuilder.loadTexts:
    ieee8021FrerPerPortPerStreamCountersEntry.setStatus("current")
_Ieee8021FrerPerPortPerStreamDirection_Type = TruthValue
_Ieee8021FrerPerPortPerStreamDirection_Object = MibTableColumn
ieee8021FrerPerPortPerStreamDirection = _Ieee8021FrerPerPortPerStreamDirection_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 17, 17, 1, 1),
    _Ieee8021FrerPerPortPerStreamDirection_Type()
)
ieee8021FrerPerPortPerStreamDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021FrerPerPortPerStreamDirection.setStatus("current")
_Ieee8021FrerPerPortPerStreamSeqGenResets_Type = Counter64
_Ieee8021FrerPerPortPerStreamSeqGenResets_Object = MibTableColumn
ieee8021FrerPerPortPerStreamSeqGenResets = _Ieee8021FrerPerPortPerStreamSeqGenResets_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 17, 17, 1, 2),
    _Ieee8021FrerPerPortPerStreamSeqGenResets_Type()
)
ieee8021FrerPerPortPerStreamSeqGenResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FrerPerPortPerStreamSeqGenResets.setStatus("current")
_Ieee8021FrerPerPortPerStreamSeqRecoveryOutOfOrderPackets_Type = Counter64
_Ieee8021FrerPerPortPerStreamSeqRecoveryOutOfOrderPackets_Object = MibTableColumn
ieee8021FrerPerPortPerStreamSeqRecoveryOutOfOrderPackets = _Ieee8021FrerPerPortPerStreamSeqRecoveryOutOfOrderPackets_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 17, 17, 1, 3),
    _Ieee8021FrerPerPortPerStreamSeqRecoveryOutOfOrderPackets_Type()
)
ieee8021FrerPerPortPerStreamSeqRecoveryOutOfOrderPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FrerPerPortPerStreamSeqRecoveryOutOfOrderPackets.setStatus("current")
_Ieee8021FrerPerPortPerStreamSeqRecoveryRoguePackets_Type = Counter64
_Ieee8021FrerPerPortPerStreamSeqRecoveryRoguePackets_Object = MibTableColumn
ieee8021FrerPerPortPerStreamSeqRecoveryRoguePackets = _Ieee8021FrerPerPortPerStreamSeqRecoveryRoguePackets_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 17, 17, 1, 4),
    _Ieee8021FrerPerPortPerStreamSeqRecoveryRoguePackets_Type()
)
ieee8021FrerPerPortPerStreamSeqRecoveryRoguePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FrerPerPortPerStreamSeqRecoveryRoguePackets.setStatus("current")
_Ieee8021FrerPerPortPerStreamSeqRecoveryPassedPackets_Type = Counter64
_Ieee8021FrerPerPortPerStreamSeqRecoveryPassedPackets_Object = MibTableColumn
ieee8021FrerPerPortPerStreamSeqRecoveryPassedPackets = _Ieee8021FrerPerPortPerStreamSeqRecoveryPassedPackets_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 17, 17, 1, 5),
    _Ieee8021FrerPerPortPerStreamSeqRecoveryPassedPackets_Type()
)
ieee8021FrerPerPortPerStreamSeqRecoveryPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FrerPerPortPerStreamSeqRecoveryPassedPackets.setStatus("current")
_Ieee8021FrerPerPortPerStreamSeqRecoveryDiscardedPackets_Type = Counter64
_Ieee8021FrerPerPortPerStreamSeqRecoveryDiscardedPackets_Object = MibTableColumn
ieee8021FrerPerPortPerStreamSeqRecoveryDiscardedPackets = _Ieee8021FrerPerPortPerStreamSeqRecoveryDiscardedPackets_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 17, 17, 1, 6),
    _Ieee8021FrerPerPortPerStreamSeqRecoveryDiscardedPackets_Type()
)
ieee8021FrerPerPortPerStreamSeqRecoveryDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FrerPerPortPerStreamSeqRecoveryDiscardedPackets.setStatus("current")
_Ieee8021FrerPerPortPerStreamSeqRecoveryLostPackets_Type = Counter64
_Ieee8021FrerPerPortPerStreamSeqRecoveryLostPackets_Object = MibTableColumn
ieee8021FrerPerPortPerStreamSeqRecoveryLostPackets = _Ieee8021FrerPerPortPerStreamSeqRecoveryLostPackets_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 17, 17, 1, 7),
    _Ieee8021FrerPerPortPerStreamSeqRecoveryLostPackets_Type()
)
ieee8021FrerPerPortPerStreamSeqRecoveryLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FrerPerPortPerStreamSeqRecoveryLostPackets.setStatus("current")
_Ieee8021FrerPerPortPerStreamSeqRecoveryTaglessPackets_Type = Counter64
_Ieee8021FrerPerPortPerStreamSeqRecoveryTaglessPackets_Object = MibTableColumn
ieee8021FrerPerPortPerStreamSeqRecoveryTaglessPackets = _Ieee8021FrerPerPortPerStreamSeqRecoveryTaglessPackets_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 17, 17, 1, 8),
    _Ieee8021FrerPerPortPerStreamSeqRecoveryTaglessPackets_Type()
)
ieee8021FrerPerPortPerStreamSeqRecoveryTaglessPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FrerPerPortPerStreamSeqRecoveryTaglessPackets.setStatus("current")
_Ieee8021FrerPerPortPerStreamSeqRecoveryResets_Type = Counter64
_Ieee8021FrerPerPortPerStreamSeqRecoveryResets_Object = MibTableColumn
ieee8021FrerPerPortPerStreamSeqRecoveryResets = _Ieee8021FrerPerPortPerStreamSeqRecoveryResets_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 17, 17, 1, 9),
    _Ieee8021FrerPerPortPerStreamSeqRecoveryResets_Type()
)
ieee8021FrerPerPortPerStreamSeqRecoveryResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FrerPerPortPerStreamSeqRecoveryResets.setStatus("current")
_Ieee8021FrerPerPortPerStreamSeqRecoveryLatentErrorResets_Type = Counter64
_Ieee8021FrerPerPortPerStreamSeqRecoveryLatentErrorResets_Object = MibTableColumn
ieee8021FrerPerPortPerStreamSeqRecoveryLatentErrorResets = _Ieee8021FrerPerPortPerStreamSeqRecoveryLatentErrorResets_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 17, 17, 1, 10),
    _Ieee8021FrerPerPortPerStreamSeqRecoveryLatentErrorResets_Type()
)
ieee8021FrerPerPortPerStreamSeqRecoveryLatentErrorResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FrerPerPortPerStreamSeqRecoveryLatentErrorResets.setStatus("current")
_Ieee8021FrerPerPortPerStreamSeqEncErroredPackets_Type = Counter64
_Ieee8021FrerPerPortPerStreamSeqEncErroredPackets_Object = MibTableColumn
ieee8021FrerPerPortPerStreamSeqEncErroredPackets = _Ieee8021FrerPerPortPerStreamSeqEncErroredPackets_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 17, 17, 1, 11),
    _Ieee8021FrerPerPortPerStreamSeqEncErroredPackets_Type()
)
ieee8021FrerPerPortPerStreamSeqEncErroredPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FrerPerPortPerStreamSeqEncErroredPackets.setStatus("current")
_Ieee8021FrerPerPortCounters_ObjectIdentity = ObjectIdentity
ieee8021FrerPerPortCounters = _Ieee8021FrerPerPortCounters_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 18)
)
_Ieee8021FrerPerPortCountersTable_Object = MibTable
ieee8021FrerPerPortCountersTable = _Ieee8021FrerPerPortCountersTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 18, 18)
)
if mibBuilder.loadTexts:
    ieee8021FrerPerPortCountersTable.setStatus("current")
_Ieee8021FrerPerPortCountersEntry_Object = MibTableRow
ieee8021FrerPerPortCountersEntry = _Ieee8021FrerPerPortCountersEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 18, 18, 1)
)
ieee8021FrerPerPortCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ieee8021FrerPerPortCountersEntry.setStatus("current")
_Ieee8021FrerPerPortSeqRecoveryPassedPackets_Type = Counter64
_Ieee8021FrerPerPortSeqRecoveryPassedPackets_Object = MibTableColumn
ieee8021FrerPerPortSeqRecoveryPassedPackets = _Ieee8021FrerPerPortSeqRecoveryPassedPackets_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 18, 18, 1, 1),
    _Ieee8021FrerPerPortSeqRecoveryPassedPackets_Type()
)
ieee8021FrerPerPortSeqRecoveryPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FrerPerPortSeqRecoveryPassedPackets.setStatus("current")
_Ieee8021FrerPerPortfrerCpSeqRecoveryDiscardPackets_Type = Counter64
_Ieee8021FrerPerPortfrerCpSeqRecoveryDiscardPackets_Object = MibTableColumn
ieee8021FrerPerPortfrerCpSeqRecoveryDiscardPackets = _Ieee8021FrerPerPortfrerCpSeqRecoveryDiscardPackets_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 18, 18, 1, 2),
    _Ieee8021FrerPerPortfrerCpSeqRecoveryDiscardPackets_Type()
)
ieee8021FrerPerPortfrerCpSeqRecoveryDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FrerPerPortfrerCpSeqRecoveryDiscardPackets.setStatus("current")
_Ieee8021FrerPerPortfrerCpSeqEncErroredPackets_Type = Counter64
_Ieee8021FrerPerPortfrerCpSeqEncErroredPackets_Object = MibTableColumn
ieee8021FrerPerPortfrerCpSeqEncErroredPackets = _Ieee8021FrerPerPortfrerCpSeqEncErroredPackets_Object(
    (1, 3, 111, 2, 802, 1, 1, 35, 1, 18, 18, 1, 3),
    _Ieee8021FrerPerPortfrerCpSeqEncErroredPackets_Type()
)
ieee8021FrerPerPortfrerCpSeqEncErroredPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FrerPerPortfrerCpSeqEncErroredPackets.setStatus("current")
_Ieee8021FrerConformance_ObjectIdentity = ObjectIdentity
ieee8021FrerConformance = _Ieee8021FrerConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 2)
)
_Ieee8021FrerCompliances_ObjectIdentity = ObjectIdentity
ieee8021FrerCompliances = _Ieee8021FrerCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 2, 1)
)
_Ieee8021FrerGroups_ObjectIdentity = ObjectIdentity
ieee8021FrerGroups = _Ieee8021FrerGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 35, 2, 2)
)

# Managed Objects groups

ieee8021FrerSequenceGenerationGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 35, 2, 2, 1)
)
ieee8021FrerSequenceGenerationGroup.setObjects(
      *(("IEEE8021-FRER-MIB", "ieee8021FrerSequenceGenerationStreamList"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceGenerationDirection"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceGenerationReset"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceGenerationStreamHandle"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceGenerationHandleListStatus"))
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceGenerationGroup.setStatus("current")

ieee8021FrerSequenceRecoveryGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 35, 2, 2, 2)
)
ieee8021FrerSequenceRecoveryGroup.setObjects(
      *(("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryStreamList"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryPortList"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryDirection"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryReset"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryAlgorithm"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryAlgorithmOUI"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceCustomRecoveryAlgorithm"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceCustomRecoveryAlgorithmOUI"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryHistoryLength"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryResetMSec"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryInvalidSequenceValue"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryTakeNoSequence"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryIndividualRecovery"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryLatentErrorDetection"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryLatentErrorDifference"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryLatentErrorPeriod"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryLatentErrorPaths"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryLatentResetPeriod"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryStatus"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryStreamHandle"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryHandleListStatus"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryPortHandle"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryPortHandleListStatus"))
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceRecoveryGroup.setStatus("current")

ieee8021FrerSequenceIdentificationGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 35, 2, 2, 3)
)
ieee8021FrerSequenceIdentificationGroup.setObjects(
      *(("IEEE8021-FRER-MIB", "ieee8021FrerSequenceIdentificationStreamList"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceIdentificationEncodeActive"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceIdentificationEncodeEncapsulationType"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceIdentificationEncodeEncapsulationOUI"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationType"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationOUI"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceIdentificationEncodePathIdLanId"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceIdentificationStatus"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceIdentificationStreamHandle"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceIdentificationHandleListStatus"))
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceIdentificationGroup.setStatus("current")

ieee8021FrerStreamSplitGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 35, 2, 2, 4)
)
ieee8021FrerStreamSplitGroup.setObjects(
      *(("IEEE8021-FRER-MIB", "ieee8021FrerStreamSplitPort"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerStreamSplitDirection"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerStreamSplitInputIdList"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerStreamSplitOutputIdList"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerStreamSplitInputIdHandle"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerStreamSplitInputHandleListStatus"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerStreamSplitOutputIdHandle"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerStreamSplitOutputHandleListStatus"))
)
if mibBuilder.loadTexts:
    ieee8021FrerStreamSplitGroup.setStatus("current")

ieee8021FrerSequenceAutoconfigGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 35, 2, 2, 5)
)
ieee8021FrerSequenceAutoconfigGroup.setObjects(
      *(("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigSequenceEncapsulation"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigSequenceEncapsulationOUI"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigCustomSequenceEncapsulation"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigCustomSequenceEncOUI"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigReceivePortList"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigTagged"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigVlanList"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigRecoveryPortList"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigDestructMSec"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigResetMSec"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigAlgorithm"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigAlgorithmOUI"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigCustomAlgorithm"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigCustomAlgorithmOUI"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigHistoryLength"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigCreateIndividual"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigCreateRecovery"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigLatentErrorDetection"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigLatentErrorDifference"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigLatentErrorPeriod"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigLatentErrorResetPeriod"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigStatus"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigReceivePortHandle"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigReceivePortHandleListStatus"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigVlan"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigVlanListStatus"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigRecoveryPortHandle"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigRecoveryPortHandleListStatus"))
)
if mibBuilder.loadTexts:
    ieee8021FrerSequenceAutoconfigGroup.setStatus("current")

ieee8021FrerOutputAutoconfigGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 35, 2, 2, 6)
)
ieee8021FrerOutputAutoconfigGroup.setObjects(
      *(("IEEE8021-FRER-MIB", "ieee8021FrerOutputAutoconfigPortList"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerOutputAutoconfigEncapsulation"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerOutputAutoconfigEncapsulationOUI"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerOutputAutoconfigCustomEncapsulation"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerOutputAutoconfigCustomEncapsulationOUI"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerOutputAutoconfigLanPathId"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerOutputAutoconfigStatus"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerOutputAutoconfigPortHandle"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerOutputAutoconfigPortHandleListStatus"))
)
if mibBuilder.loadTexts:
    ieee8021FrerOutputAutoconfigGroup.setStatus("current")

ieee8021FrerPerPortPerStreamCountersGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 35, 2, 2, 7)
)
ieee8021FrerPerPortPerStreamCountersGroup.setObjects(
      *(("IEEE8021-FRER-MIB", "ieee8021FrerPerPortPerStreamSeqGenResets"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerPerPortPerStreamSeqRecoveryOutOfOrderPackets"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerPerPortPerStreamSeqRecoveryRoguePackets"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerPerPortPerStreamSeqRecoveryPassedPackets"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerPerPortPerStreamSeqRecoveryDiscardedPackets"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerPerPortPerStreamSeqRecoveryLostPackets"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerPerPortPerStreamSeqRecoveryTaglessPackets"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerPerPortPerStreamSeqRecoveryResets"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerPerPortPerStreamSeqRecoveryLatentErrorResets"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerPerPortPerStreamSeqEncErroredPackets"))
)
if mibBuilder.loadTexts:
    ieee8021FrerPerPortPerStreamCountersGroup.setStatus("current")

ieee8021FrerPerPortCountersGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 35, 2, 2, 8)
)
ieee8021FrerPerPortCountersGroup.setObjects(
      *(("IEEE8021-FRER-MIB", "ieee8021FrerPerPortSeqRecoveryPassedPackets"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerPerPortfrerCpSeqRecoveryDiscardPackets"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerPerPortfrerCpSeqEncErroredPackets"))
)
if mibBuilder.loadTexts:
    ieee8021FrerPerPortCountersGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021FrerCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 35, 2, 1, 1)
)
ieee8021FrerCompliance.setObjects(
      *(("IEEE8021-FRER-MIB", "ieee8021FrerSequenceGenerationGroup"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceRecoveryGroup"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceIdentificationGroup"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerStreamSplitGroup"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerPerPortPerStreamCountersGroup"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerPerPortCountersGroup"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerSequenceAutoconfigGroup"),
        ("IEEE8021-FRER-MIB", "ieee8021FrerOutputAutoconfigGroup"))
)
if mibBuilder.loadTexts:
    ieee8021FrerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-FRER-MIB",
    **{"Ieee8021CBSequenceRecoveryAlgorithm": Ieee8021CBSequenceRecoveryAlgorithm,
       "Ieee8021CBSequenceEncodeDecodeType": Ieee8021CBSequenceEncodeDecodeType,
       "ieee8021FrerMib": ieee8021FrerMib,
       "ieee8021FrerNotifications": ieee8021FrerNotifications,
       "ieee8021FrerObjects": ieee8021FrerObjects,
       "ieee8021FrerSequenceGeneration": ieee8021FrerSequenceGeneration,
       "ieee8021FrerSequenceGenerationTable": ieee8021FrerSequenceGenerationTable,
       "ieee8021FrerSequenceGenerationEntry": ieee8021FrerSequenceGenerationEntry,
       "ieee8021FrerSequenceGenerationIndex": ieee8021FrerSequenceGenerationIndex,
       "ieee8021FrerSequenceGenerationStreamList": ieee8021FrerSequenceGenerationStreamList,
       "ieee8021FrerSequenceGenerationDirection": ieee8021FrerSequenceGenerationDirection,
       "ieee8021FrerSequenceGenerationReset": ieee8021FrerSequenceGenerationReset,
       "ieee8021FrerSequenceGenerationHandleList": ieee8021FrerSequenceGenerationHandleList,
       "ieee8021FrerSequenceGenerationHandleListTable": ieee8021FrerSequenceGenerationHandleListTable,
       "ieee8021FrerSequenceGenerationHandleListEntry": ieee8021FrerSequenceGenerationHandleListEntry,
       "ieee8021FrerSequenceGenerationHandleListIndex": ieee8021FrerSequenceGenerationHandleListIndex,
       "ieee8021FrerSequenceGenerationStreamHandle": ieee8021FrerSequenceGenerationStreamHandle,
       "ieee8021FrerSequenceGenerationHandleListStatus": ieee8021FrerSequenceGenerationHandleListStatus,
       "ieee8021FrerSequenceRecovery": ieee8021FrerSequenceRecovery,
       "ieee8021FrerSequenceRecoveryTable": ieee8021FrerSequenceRecoveryTable,
       "ieee8021FrerSequenceRecoveryEntry": ieee8021FrerSequenceRecoveryEntry,
       "ieee8021FrerSequenceRecoveryIndex": ieee8021FrerSequenceRecoveryIndex,
       "ieee8021FrerSequenceRecoveryStreamList": ieee8021FrerSequenceRecoveryStreamList,
       "ieee8021FrerSequenceRecoveryPortList": ieee8021FrerSequenceRecoveryPortList,
       "ieee8021FrerSequenceRecoveryDirection": ieee8021FrerSequenceRecoveryDirection,
       "ieee8021FrerSequenceRecoveryReset": ieee8021FrerSequenceRecoveryReset,
       "ieee8021FrerSequenceRecoveryAlgorithm": ieee8021FrerSequenceRecoveryAlgorithm,
       "ieee8021FrerSequenceRecoveryAlgorithmOUI": ieee8021FrerSequenceRecoveryAlgorithmOUI,
       "ieee8021FrerSequenceCustomRecoveryAlgorithm": ieee8021FrerSequenceCustomRecoveryAlgorithm,
       "ieee8021FrerSequenceCustomRecoveryAlgorithmOUI": ieee8021FrerSequenceCustomRecoveryAlgorithmOUI,
       "ieee8021FrerSequenceRecoveryHistoryLength": ieee8021FrerSequenceRecoveryHistoryLength,
       "ieee8021FrerSequenceRecoveryResetMSec": ieee8021FrerSequenceRecoveryResetMSec,
       "ieee8021FrerSequenceRecoveryInvalidSequenceValue": ieee8021FrerSequenceRecoveryInvalidSequenceValue,
       "ieee8021FrerSequenceRecoveryTakeNoSequence": ieee8021FrerSequenceRecoveryTakeNoSequence,
       "ieee8021FrerSequenceRecoveryIndividualRecovery": ieee8021FrerSequenceRecoveryIndividualRecovery,
       "ieee8021FrerSequenceRecoveryLatentErrorDetection": ieee8021FrerSequenceRecoveryLatentErrorDetection,
       "ieee8021FrerSequenceRecoveryLatentErrorDifference": ieee8021FrerSequenceRecoveryLatentErrorDifference,
       "ieee8021FrerSequenceRecoveryLatentErrorPeriod": ieee8021FrerSequenceRecoveryLatentErrorPeriod,
       "ieee8021FrerSequenceRecoveryLatentErrorPaths": ieee8021FrerSequenceRecoveryLatentErrorPaths,
       "ieee8021FrerSequenceRecoveryLatentResetPeriod": ieee8021FrerSequenceRecoveryLatentResetPeriod,
       "ieee8021FrerSequenceRecoveryStatus": ieee8021FrerSequenceRecoveryStatus,
       "ieee8021FrerSequenceRecoveryHandleList": ieee8021FrerSequenceRecoveryHandleList,
       "ieee8021FrerSequenceRecoveryHandleListTable": ieee8021FrerSequenceRecoveryHandleListTable,
       "ieee8021FrerSequenceRecoveryHandleListEntry": ieee8021FrerSequenceRecoveryHandleListEntry,
       "ieee8021FrerSequenceRecoveryHandleListIndex": ieee8021FrerSequenceRecoveryHandleListIndex,
       "ieee8021FrerSequenceRecoveryStreamHandle": ieee8021FrerSequenceRecoveryStreamHandle,
       "ieee8021FrerSequenceRecoveryHandleListStatus": ieee8021FrerSequenceRecoveryHandleListStatus,
       "ieee8021FrerSequenceRecoveryPortHandleList": ieee8021FrerSequenceRecoveryPortHandleList,
       "ieee8021FrerSequenceRecoveryPortHandleListTable": ieee8021FrerSequenceRecoveryPortHandleListTable,
       "ieee8021FrerSequenceRecoveryPortHandleListEntry": ieee8021FrerSequenceRecoveryPortHandleListEntry,
       "ieee8021FrerSequenceRecoveryPortHandleListIndex": ieee8021FrerSequenceRecoveryPortHandleListIndex,
       "ieee8021FrerSequenceRecoveryPortHandle": ieee8021FrerSequenceRecoveryPortHandle,
       "ieee8021FrerSequenceRecoveryPortHandleListStatus": ieee8021FrerSequenceRecoveryPortHandleListStatus,
       "ieee8021FrerSequenceIdentification": ieee8021FrerSequenceIdentification,
       "ieee8021FrerSequenceIdentificationTable": ieee8021FrerSequenceIdentificationTable,
       "ieee8021FrerSequenceIdentificationEntry": ieee8021FrerSequenceIdentificationEntry,
       "ieee8021FrerSequenceIdentificationEncodePort": ieee8021FrerSequenceIdentificationEncodePort,
       "ieee8021FrerSequenceIdentificationEncodeDirection": ieee8021FrerSequenceIdentificationEncodeDirection,
       "ieee8021FrerSequenceIdentificationStreamList": ieee8021FrerSequenceIdentificationStreamList,
       "ieee8021FrerSequenceIdentificationEncodeActive": ieee8021FrerSequenceIdentificationEncodeActive,
       "ieee8021FrerSequenceIdentificationEncodeEncapsulationType": ieee8021FrerSequenceIdentificationEncodeEncapsulationType,
       "ieee8021FrerSequenceIdentificationEncodeEncapsulationOUI": ieee8021FrerSequenceIdentificationEncodeEncapsulationOUI,
       "ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationType": ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationType,
       "ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationOUI": ieee8021FrerSequenceIdentificationCustomEncodeEncapsulationOUI,
       "ieee8021FrerSequenceIdentificationEncodePathIdLanId": ieee8021FrerSequenceIdentificationEncodePathIdLanId,
       "ieee8021FrerSequenceIdentificationStatus": ieee8021FrerSequenceIdentificationStatus,
       "ieee8021FrerSequenceIdentificationHandleList": ieee8021FrerSequenceIdentificationHandleList,
       "ieee8021FrerSequenceIdentificationHandleListTable": ieee8021FrerSequenceIdentificationHandleListTable,
       "ieee8021FrerSequenceIdentificationHandleListEntry": ieee8021FrerSequenceIdentificationHandleListEntry,
       "ieee8021FrerSequenceIdentificationHandleListIndex": ieee8021FrerSequenceIdentificationHandleListIndex,
       "ieee8021FrerSequenceIdentificationStreamHandle": ieee8021FrerSequenceIdentificationStreamHandle,
       "ieee8021FrerSequenceIdentificationHandleListStatus": ieee8021FrerSequenceIdentificationHandleListStatus,
       "ieee8021FrerStreamSplit": ieee8021FrerStreamSplit,
       "ieee8021FrerStreamSplitTable": ieee8021FrerStreamSplitTable,
       "ieee8021FrerStreamSplitEntry": ieee8021FrerStreamSplitEntry,
       "ieee8021FrerStreamSplitIndex": ieee8021FrerStreamSplitIndex,
       "ieee8021FrerStreamSplitPort": ieee8021FrerStreamSplitPort,
       "ieee8021FrerStreamSplitDirection": ieee8021FrerStreamSplitDirection,
       "ieee8021FrerStreamSplitInputIdList": ieee8021FrerStreamSplitInputIdList,
       "ieee8021FrerStreamSplitOutputIdList": ieee8021FrerStreamSplitOutputIdList,
       "ieee8021FrerStreamSplitInputHandleList": ieee8021FrerStreamSplitInputHandleList,
       "ieee8021FrerStreamSplitInputHandleListTable": ieee8021FrerStreamSplitInputHandleListTable,
       "ieee8021FrerStreamSplitInputHandleListEntry": ieee8021FrerStreamSplitInputHandleListEntry,
       "ieee8021FrerStreamSplitInputHandleListIndex": ieee8021FrerStreamSplitInputHandleListIndex,
       "ieee8021FrerStreamSplitInputIdHandle": ieee8021FrerStreamSplitInputIdHandle,
       "ieee8021FrerStreamSplitInputHandleListStatus": ieee8021FrerStreamSplitInputHandleListStatus,
       "ieee8021FrerStreamSplitOutputHandleList": ieee8021FrerStreamSplitOutputHandleList,
       "ieee8021FrerStreamSplitOutputHandleListTable": ieee8021FrerStreamSplitOutputHandleListTable,
       "ieee8021FrerStreamSplitOutputHandleListEntry": ieee8021FrerStreamSplitOutputHandleListEntry,
       "ieee8021FrerStreamSplitOutputHandleListIndex": ieee8021FrerStreamSplitOutputHandleListIndex,
       "ieee8021FrerStreamSplitOutputIdHandle": ieee8021FrerStreamSplitOutputIdHandle,
       "ieee8021FrerStreamSplitOutputHandleListStatus": ieee8021FrerStreamSplitOutputHandleListStatus,
       "ieee8021FrerSequenceAutoconfig": ieee8021FrerSequenceAutoconfig,
       "ieee8021FrerSequenceAutoconfigTable": ieee8021FrerSequenceAutoconfigTable,
       "ieee8021FrerSequenceAutoconfigEntry": ieee8021FrerSequenceAutoconfigEntry,
       "ieee8021FrerSequenceAutoconfigIndex": ieee8021FrerSequenceAutoconfigIndex,
       "ieee8021FrerSequenceAutoconfigSequenceEncapsulation": ieee8021FrerSequenceAutoconfigSequenceEncapsulation,
       "ieee8021FrerSequenceAutoconfigSequenceEncapsulationOUI": ieee8021FrerSequenceAutoconfigSequenceEncapsulationOUI,
       "ieee8021FrerSequenceAutoconfigCustomSequenceEncapsulation": ieee8021FrerSequenceAutoconfigCustomSequenceEncapsulation,
       "ieee8021FrerSequenceAutoconfigCustomSequenceEncOUI": ieee8021FrerSequenceAutoconfigCustomSequenceEncOUI,
       "ieee8021FrerSequenceAutoconfigReceivePortList": ieee8021FrerSequenceAutoconfigReceivePortList,
       "ieee8021FrerSequenceAutoconfigTagged": ieee8021FrerSequenceAutoconfigTagged,
       "ieee8021FrerSequenceAutoconfigVlanList": ieee8021FrerSequenceAutoconfigVlanList,
       "ieee8021FrerSequenceAutoconfigRecoveryPortList": ieee8021FrerSequenceAutoconfigRecoveryPortList,
       "ieee8021FrerSequenceAutoconfigDestructMSec": ieee8021FrerSequenceAutoconfigDestructMSec,
       "ieee8021FrerSequenceAutoconfigResetMSec": ieee8021FrerSequenceAutoconfigResetMSec,
       "ieee8021FrerSequenceAutoconfigAlgorithm": ieee8021FrerSequenceAutoconfigAlgorithm,
       "ieee8021FrerSequenceAutoconfigAlgorithmOUI": ieee8021FrerSequenceAutoconfigAlgorithmOUI,
       "ieee8021FrerSequenceAutoconfigCustomAlgorithm": ieee8021FrerSequenceAutoconfigCustomAlgorithm,
       "ieee8021FrerSequenceAutoconfigCustomAlgorithmOUI": ieee8021FrerSequenceAutoconfigCustomAlgorithmOUI,
       "ieee8021FrerSequenceAutoconfigHistoryLength": ieee8021FrerSequenceAutoconfigHistoryLength,
       "ieee8021FrerSequenceAutoconfigCreateIndividual": ieee8021FrerSequenceAutoconfigCreateIndividual,
       "ieee8021FrerSequenceAutoconfigCreateRecovery": ieee8021FrerSequenceAutoconfigCreateRecovery,
       "ieee8021FrerSequenceAutoconfigLatentErrorDetection": ieee8021FrerSequenceAutoconfigLatentErrorDetection,
       "ieee8021FrerSequenceAutoconfigLatentErrorDifference": ieee8021FrerSequenceAutoconfigLatentErrorDifference,
       "ieee8021FrerSequenceAutoconfigLatentErrorPeriod": ieee8021FrerSequenceAutoconfigLatentErrorPeriod,
       "ieee8021FrerSequenceAutoconfigLatentErrorResetPeriod": ieee8021FrerSequenceAutoconfigLatentErrorResetPeriod,
       "ieee8021FrerSequenceAutoconfigStatus": ieee8021FrerSequenceAutoconfigStatus,
       "ieee8021FrerSequenceAutoconfigReceivePortHandleList": ieee8021FrerSequenceAutoconfigReceivePortHandleList,
       "ieee8021FrerSequenceAutoconfigReceivePortHandleListTable": ieee8021FrerSequenceAutoconfigReceivePortHandleListTable,
       "ieee8021FrerSequenceAutoconfigReceivePortHandleListEntry": ieee8021FrerSequenceAutoconfigReceivePortHandleListEntry,
       "ieee8021FrerSequenceAutoconfigReceivePortHandleListIndex": ieee8021FrerSequenceAutoconfigReceivePortHandleListIndex,
       "ieee8021FrerSequenceAutoconfigReceivePortHandle": ieee8021FrerSequenceAutoconfigReceivePortHandle,
       "ieee8021FrerSequenceAutoconfigReceivePortHandleListStatus": ieee8021FrerSequenceAutoconfigReceivePortHandleListStatus,
       "ieee8021FrerSequenceAutoconfigVlanHandleList": ieee8021FrerSequenceAutoconfigVlanHandleList,
       "ieee8021FrerSequenceAutoconfigVlanListTable": ieee8021FrerSequenceAutoconfigVlanListTable,
       "ieee8021FrerSequenceAutoconfigVlanListEntry": ieee8021FrerSequenceAutoconfigVlanListEntry,
       "ieee8021FrerSequenceAutoconfigVlanListIndex": ieee8021FrerSequenceAutoconfigVlanListIndex,
       "ieee8021FrerSequenceAutoconfigVlan": ieee8021FrerSequenceAutoconfigVlan,
       "ieee8021FrerSequenceAutoconfigVlanListStatus": ieee8021FrerSequenceAutoconfigVlanListStatus,
       "ieee8021FrerSequenceAutoconfigRecoveryPortHandleList": ieee8021FrerSequenceAutoconfigRecoveryPortHandleList,
       "ieee8021FrerSequenceAutoconfigRecoveryPortHandleListTable": ieee8021FrerSequenceAutoconfigRecoveryPortHandleListTable,
       "ieee8021FrerSequenceAutoconfigRecoveryPortHandleListEntry": ieee8021FrerSequenceAutoconfigRecoveryPortHandleListEntry,
       "ieee8021FrerSequenceAutoconfigRecoveryPortHandleListIndex": ieee8021FrerSequenceAutoconfigRecoveryPortHandleListIndex,
       "ieee8021FrerSequenceAutoconfigRecoveryPortHandle": ieee8021FrerSequenceAutoconfigRecoveryPortHandle,
       "ieee8021FrerSequenceAutoconfigRecoveryPortHandleListStatus": ieee8021FrerSequenceAutoconfigRecoveryPortHandleListStatus,
       "ieee8021FrerOutputAutoconfig": ieee8021FrerOutputAutoconfig,
       "ieee8021FrerOutputAutoconfigTable": ieee8021FrerOutputAutoconfigTable,
       "ieee8021FrerOutputAutoconfigEntry": ieee8021FrerOutputAutoconfigEntry,
       "ieee8021FrerOutputAutoconfigIndex": ieee8021FrerOutputAutoconfigIndex,
       "ieee8021FrerOutputAutoconfigPortList": ieee8021FrerOutputAutoconfigPortList,
       "ieee8021FrerOutputAutoconfigEncapsulation": ieee8021FrerOutputAutoconfigEncapsulation,
       "ieee8021FrerOutputAutoconfigEncapsulationOUI": ieee8021FrerOutputAutoconfigEncapsulationOUI,
       "ieee8021FrerOutputAutoconfigCustomEncapsulation": ieee8021FrerOutputAutoconfigCustomEncapsulation,
       "ieee8021FrerOutputAutoconfigCustomEncapsulationOUI": ieee8021FrerOutputAutoconfigCustomEncapsulationOUI,
       "ieee8021FrerOutputAutoconfigLanPathId": ieee8021FrerOutputAutoconfigLanPathId,
       "ieee8021FrerOutputAutoconfigStatus": ieee8021FrerOutputAutoconfigStatus,
       "ieee8021FrerOutputAutoconfigPortHandleList": ieee8021FrerOutputAutoconfigPortHandleList,
       "ieee8021FrerOutputAutoconfigPortHandleListTable": ieee8021FrerOutputAutoconfigPortHandleListTable,
       "ieee8021FrerOutputAutoconfigPortHandleListEntry": ieee8021FrerOutputAutoconfigPortHandleListEntry,
       "ieee8021FrerOutputAutoconfigPortHandleListIndex": ieee8021FrerOutputAutoconfigPortHandleListIndex,
       "ieee8021FrerOutputAutoconfigPortHandle": ieee8021FrerOutputAutoconfigPortHandle,
       "ieee8021FrerOutputAutoconfigPortHandleListStatus": ieee8021FrerOutputAutoconfigPortHandleListStatus,
       "ieee8021FrerPerPortPerStreamCounters": ieee8021FrerPerPortPerStreamCounters,
       "ieee8021FrerPerPortPerStreamCountersTable": ieee8021FrerPerPortPerStreamCountersTable,
       "ieee8021FrerPerPortPerStreamCountersEntry": ieee8021FrerPerPortPerStreamCountersEntry,
       "ieee8021FrerPerPortPerStreamDirection": ieee8021FrerPerPortPerStreamDirection,
       "ieee8021FrerPerPortPerStreamSeqGenResets": ieee8021FrerPerPortPerStreamSeqGenResets,
       "ieee8021FrerPerPortPerStreamSeqRecoveryOutOfOrderPackets": ieee8021FrerPerPortPerStreamSeqRecoveryOutOfOrderPackets,
       "ieee8021FrerPerPortPerStreamSeqRecoveryRoguePackets": ieee8021FrerPerPortPerStreamSeqRecoveryRoguePackets,
       "ieee8021FrerPerPortPerStreamSeqRecoveryPassedPackets": ieee8021FrerPerPortPerStreamSeqRecoveryPassedPackets,
       "ieee8021FrerPerPortPerStreamSeqRecoveryDiscardedPackets": ieee8021FrerPerPortPerStreamSeqRecoveryDiscardedPackets,
       "ieee8021FrerPerPortPerStreamSeqRecoveryLostPackets": ieee8021FrerPerPortPerStreamSeqRecoveryLostPackets,
       "ieee8021FrerPerPortPerStreamSeqRecoveryTaglessPackets": ieee8021FrerPerPortPerStreamSeqRecoveryTaglessPackets,
       "ieee8021FrerPerPortPerStreamSeqRecoveryResets": ieee8021FrerPerPortPerStreamSeqRecoveryResets,
       "ieee8021FrerPerPortPerStreamSeqRecoveryLatentErrorResets": ieee8021FrerPerPortPerStreamSeqRecoveryLatentErrorResets,
       "ieee8021FrerPerPortPerStreamSeqEncErroredPackets": ieee8021FrerPerPortPerStreamSeqEncErroredPackets,
       "ieee8021FrerPerPortCounters": ieee8021FrerPerPortCounters,
       "ieee8021FrerPerPortCountersTable": ieee8021FrerPerPortCountersTable,
       "ieee8021FrerPerPortCountersEntry": ieee8021FrerPerPortCountersEntry,
       "ieee8021FrerPerPortSeqRecoveryPassedPackets": ieee8021FrerPerPortSeqRecoveryPassedPackets,
       "ieee8021FrerPerPortfrerCpSeqRecoveryDiscardPackets": ieee8021FrerPerPortfrerCpSeqRecoveryDiscardPackets,
       "ieee8021FrerPerPortfrerCpSeqEncErroredPackets": ieee8021FrerPerPortfrerCpSeqEncErroredPackets,
       "ieee8021FrerConformance": ieee8021FrerConformance,
       "ieee8021FrerCompliances": ieee8021FrerCompliances,
       "ieee8021FrerCompliance": ieee8021FrerCompliance,
       "ieee8021FrerGroups": ieee8021FrerGroups,
       "ieee8021FrerSequenceGenerationGroup": ieee8021FrerSequenceGenerationGroup,
       "ieee8021FrerSequenceRecoveryGroup": ieee8021FrerSequenceRecoveryGroup,
       "ieee8021FrerSequenceIdentificationGroup": ieee8021FrerSequenceIdentificationGroup,
       "ieee8021FrerStreamSplitGroup": ieee8021FrerStreamSplitGroup,
       "ieee8021FrerSequenceAutoconfigGroup": ieee8021FrerSequenceAutoconfigGroup,
       "ieee8021FrerOutputAutoconfigGroup": ieee8021FrerOutputAutoconfigGroup,
       "ieee8021FrerPerPortPerStreamCountersGroup": ieee8021FrerPerPortPerStreamCountersGroup,
       "ieee8021FrerPerPortCountersGroup": ieee8021FrerPerPortCountersGroup}
)
