# SNMP MIB module (TROPIC-PTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-PTP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:04:12 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

tnPtpMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 4, 7)
)
if mibBuilder.loadTexts:
    tnPtpMibModule.setRevisions(
        ("2016-09-21 15:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class InetAddressType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("dns", 16))
    )



class InetAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class AluWdmPtpClockIdentifier(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class AluWdmPtpClockIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class AluWdmPtpRecoveredClockState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("freeRun", 1),
          ("acquiring", 2),
          ("phasetracking", 3),
          ("holdover", 4),
          ("locked", 5))
    )



class AluWdmtnPtpPortState(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("initializing", 1),
          ("faulty", 2),
          ("disabled", 3),
          ("listening", 4),
          ("premaster", 5),
          ("master", 6),
          ("passive", 7),
          ("uncalibrated", 8),
          ("slave", 9))
    )



class TropicSlotIndexType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 142),
    )



class TropicShelfIndexType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )



# MIB Managed Objects in the order of their OIDs

_Tropic_ObjectIdentity = ObjectIdentity
tropic = _Tropic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483)
)
if mibBuilder.loadTexts:
    tropic.setStatus("current")
_TropicRegistry_ObjectIdentity = ObjectIdentity
tropicRegistry = _TropicRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1)
)
if mibBuilder.loadTexts:
    tropicRegistry.setStatus("current")
_TropicModules_ObjectIdentity = ObjectIdentity
tropicModules = _TropicModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1)
)
if mibBuilder.loadTexts:
    tropicModules.setStatus("current")
_TnGenericModules_ObjectIdentity = ObjectIdentity
tnGenericModules = _TnGenericModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnGenericModules.setStatus("current")
_TnEquipmentModules_ObjectIdentity = ObjectIdentity
tnEquipmentModules = _TnEquipmentModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tnEquipmentModules.setStatus("current")
_TnPortModules_ObjectIdentity = ObjectIdentity
tnPortModules = _TnPortModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    tnPortModules.setStatus("current")
_TropicGeneric_ObjectIdentity = ObjectIdentity
tropicGeneric = _TropicGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2)
)
if mibBuilder.loadTexts:
    tropicGeneric.setStatus("current")
_TnEquipment_ObjectIdentity = ObjectIdentity
tnEquipment = _TnEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2)
)
if mibBuilder.loadTexts:
    tnEquipment.setStatus("current")
_TnShelf_ObjectIdentity = ObjectIdentity
tnShelf = _TnShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnShelf.setStatus("current")
_TnShelfMIB_ObjectIdentity = ObjectIdentity
tnShelfMIB = _TnShelfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnShelfMIB.setStatus("current")
_TnShelfObjs_ObjectIdentity = ObjectIdentity
tnShelfObjs = _TnShelfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2)
)
_TnShelfBasics_ObjectIdentity = ObjectIdentity
tnShelfBasics = _TnShelfBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1)
)
_TnShelfTable_Object = MibTable
tnShelfTable = _TnShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnShelfTable.setStatus("current")
_TnShelfEntry_Object = MibTableRow
tnShelfEntry = _TnShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1)
)
tnShelfEntry.setIndexNames(
    (0, "TROPIC-PTP-MIB", "tnShelfIndex"),
)
if mibBuilder.loadTexts:
    tnShelfEntry.setStatus("current")
_TnShelfIndex_Type = TropicShelfIndexType
_TnShelfIndex_Object = MibTableColumn
tnShelfIndex = _TnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 1, 1, 2, 1, 1, 1, 1),
    _TnShelfIndex_Type()
)
tnShelfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnShelfIndex.setStatus("current")
_TnSlot_ObjectIdentity = ObjectIdentity
tnSlot = _TnSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tnSlot.setStatus("current")
_TnSlotMIB_ObjectIdentity = ObjectIdentity
tnSlotMIB = _TnSlotMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnSlotMIB.setStatus("current")
_TnSlotObjs_ObjectIdentity = ObjectIdentity
tnSlotObjs = _TnSlotObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2)
)
_TnSlotBasics_ObjectIdentity = ObjectIdentity
tnSlotBasics = _TnSlotBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2)
)
_TnSlotTable_Object = MibTable
tnSlotTable = _TnSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnSlotTable.setStatus("current")
_TnSlotEntry_Object = MibTableRow
tnSlotEntry = _TnSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1)
)
tnSlotEntry.setIndexNames(
    (0, "TROPIC-PTP-MIB", "tnShelfIndex"),
    (0, "TROPIC-PTP-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSlotEntry.setStatus("current")
_TnSlotIndex_Type = TropicSlotIndexType
_TnSlotIndex_Object = MibTableColumn
tnSlotIndex = _TnSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 2, 1, 2, 2, 1, 1, 1),
    _TnSlotIndex_Type()
)
tnSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSlotIndex.setStatus("current")
_TnPort_ObjectIdentity = ObjectIdentity
tnPort = _TnPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4)
)
if mibBuilder.loadTexts:
    tnPort.setStatus("current")
_TnPtpMIB_ObjectIdentity = ObjectIdentity
tnPtpMIB = _TnPtpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9)
)
if mibBuilder.loadTexts:
    tnPtpMIB.setStatus("current")
_TnPtpMIBObjects_ObjectIdentity = ObjectIdentity
tnPtpMIBObjects = _TnPtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1)
)
_TnPtpSystem_ObjectIdentity = ObjectIdentity
tnPtpSystem = _TnPtpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 1)
)
_TnPtpSystemTable_Object = MibTable
tnPtpSystemTable = _TnPtpSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnPtpSystemTable.setStatus("current")
_TnPtpSystemEntry_Object = MibTableRow
tnPtpSystemEntry = _TnPtpSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 1, 1, 1)
)
tnPtpSystemEntry.setIndexNames(
    (0, "TROPIC-PTP-MIB", "tnShelfIndex"),
    (0, "TROPIC-PTP-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPtpSystemEntry.setStatus("current")


class _TnPtpSystemClockMode_Type(Integer32):
    """Custom type tnPtpSystemClockMode based on Integer32"""
    defaultValue = 0


_TnPtpSystemClockMode_Type.__name__ = "Integer32"
_TnPtpSystemClockMode_Object = MibTableColumn
tnPtpSystemClockMode = _TnPtpSystemClockMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 1, 1, 1, 1),
    _TnPtpSystemClockMode_Type()
)
tnPtpSystemClockMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpSystemClockMode.setStatus("current")


class _TnPtpSystemFrequencyReference_Type(Integer32):
    """Custom type tnPtpSystemFrequencyReference based on Integer32"""
    defaultValue = 0


_TnPtpSystemFrequencyReference_Type.__name__ = "Integer32"
_TnPtpSystemFrequencyReference_Object = MibTableColumn
tnPtpSystemFrequencyReference = _TnPtpSystemFrequencyReference_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 1, 1, 1, 2),
    _TnPtpSystemFrequencyReference_Type()
)
tnPtpSystemFrequencyReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpSystemFrequencyReference.setStatus("current")


class _TnPtpSystemTimeReference_Type(Integer32):
    """Custom type tnPtpSystemTimeReference based on Integer32"""
    defaultValue = 2


_TnPtpSystemTimeReference_Type.__name__ = "Integer32"
_TnPtpSystemTimeReference_Object = MibTableColumn
tnPtpSystemTimeReference = _TnPtpSystemTimeReference_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 1, 1, 1, 3),
    _TnPtpSystemTimeReference_Type()
)
tnPtpSystemTimeReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpSystemTimeReference.setStatus("current")
_TnPtpSystemNextClockNumber_Type = Integer32
_TnPtpSystemNextClockNumber_Object = MibTableColumn
tnPtpSystemNextClockNumber = _TnPtpSystemNextClockNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 1, 1, 1, 4),
    _TnPtpSystemNextClockNumber_Type()
)
tnPtpSystemNextClockNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpSystemNextClockNumber.setStatus("current")


class _TnPtpSystemClockProfile_Type(Integer32):
    """Custom type tnPtpSystemClockProfile based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ieee-1588-2008-CCSA", 0),
          ("g-8275-1", 1))
    )


_TnPtpSystemClockProfile_Type.__name__ = "Integer32"
_TnPtpSystemClockProfile_Object = MibTableColumn
tnPtpSystemClockProfile = _TnPtpSystemClockProfile_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 1, 1, 1, 5),
    _TnPtpSystemClockProfile_Type()
)
tnPtpSystemClockProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpSystemClockProfile.setStatus("current")


class _TnPtpSystemClockServoMode_Type(Integer32):
    """Custom type tnPtpSystemClockServoMode based on Integer32"""
    defaultValue = 0


_TnPtpSystemClockServoMode_Type.__name__ = "Integer32"
_TnPtpSystemClockServoMode_Object = MibTableColumn
tnPtpSystemClockServoMode = _TnPtpSystemClockServoMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 1, 1, 1, 6),
    _TnPtpSystemClockServoMode_Type()
)
tnPtpSystemClockServoMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpSystemClockServoMode.setStatus("current")
_TnPtpClock_ObjectIdentity = ObjectIdentity
tnPtpClock = _TnPtpClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2)
)
_TnPtpClockDefaultDSConfigTable_Object = MibTable
tnPtpClockDefaultDSConfigTable = _TnPtpClockDefaultDSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSConfigTable.setStatus("current")
_TnPtpClockDefaultDSConfigEntry_Object = MibTableRow
tnPtpClockDefaultDSConfigEntry = _TnPtpClockDefaultDSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 1, 1)
)
tnPtpClockDefaultDSConfigEntry.setIndexNames(
    (0, "TROPIC-PTP-MIB", "tnPtpClockIndex"),
)
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSConfigEntry.setStatus("current")
_TnPtpClockIndex_Type = AluWdmPtpClockIndex
_TnPtpClockIndex_Object = MibTableColumn
tnPtpClockIndex = _TnPtpClockIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 1, 1, 1),
    _TnPtpClockIndex_Type()
)
tnPtpClockIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPtpClockIndex.setStatus("current")


class _TnPtpClockDefaultDSConfigDomain_Type(Unsigned32):
    """Custom type tnPtpClockDefaultDSConfigDomain based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnPtpClockDefaultDSConfigDomain_Type.__name__ = "Unsigned32"
_TnPtpClockDefaultDSConfigDomain_Object = MibTableColumn
tnPtpClockDefaultDSConfigDomain = _TnPtpClockDefaultDSConfigDomain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 1, 1, 2),
    _TnPtpClockDefaultDSConfigDomain_Type()
)
tnPtpClockDefaultDSConfigDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSConfigDomain.setStatus("current")


class _TnPtpClockDefaultDSConfigPriority1_Type(Unsigned32):
    """Custom type tnPtpClockDefaultDSConfigPriority1 based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnPtpClockDefaultDSConfigPriority1_Type.__name__ = "Unsigned32"
_TnPtpClockDefaultDSConfigPriority1_Object = MibTableColumn
tnPtpClockDefaultDSConfigPriority1 = _TnPtpClockDefaultDSConfigPriority1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 1, 1, 3),
    _TnPtpClockDefaultDSConfigPriority1_Type()
)
tnPtpClockDefaultDSConfigPriority1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSConfigPriority1.setStatus("current")


class _TnPtpClockDefaultDSConfigPriority2_Type(Unsigned32):
    """Custom type tnPtpClockDefaultDSConfigPriority2 based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnPtpClockDefaultDSConfigPriority2_Type.__name__ = "Unsigned32"
_TnPtpClockDefaultDSConfigPriority2_Object = MibTableColumn
tnPtpClockDefaultDSConfigPriority2 = _TnPtpClockDefaultDSConfigPriority2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 1, 1, 4),
    _TnPtpClockDefaultDSConfigPriority2_Type()
)
tnPtpClockDefaultDSConfigPriority2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSConfigPriority2.setStatus("current")
_TnPtpClockDefaultDSConfigPreferedGM_Type = AluWdmPtpClockIdentifier
_TnPtpClockDefaultDSConfigPreferedGM_Object = MibTableColumn
tnPtpClockDefaultDSConfigPreferedGM = _TnPtpClockDefaultDSConfigPreferedGM_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 1, 1, 5),
    _TnPtpClockDefaultDSConfigPreferedGM_Type()
)
tnPtpClockDefaultDSConfigPreferedGM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSConfigPreferedGM.setStatus("current")


class _TnPtpClockDefaultDSConfigIpAddressType_Type(InetAddressType):
    """Custom type tnPtpClockDefaultDSConfigIpAddressType based on InetAddressType"""
    defaultValue = 1


_TnPtpClockDefaultDSConfigIpAddressType_Type.__name__ = "InetAddressType"
_TnPtpClockDefaultDSConfigIpAddressType_Object = MibTableColumn
tnPtpClockDefaultDSConfigIpAddressType = _TnPtpClockDefaultDSConfigIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 1, 1, 6),
    _TnPtpClockDefaultDSConfigIpAddressType_Type()
)
tnPtpClockDefaultDSConfigIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSConfigIpAddressType.setStatus("current")
_TnPtpClockDefaultDSConfigIpAddress_Type = InetAddress
_TnPtpClockDefaultDSConfigIpAddress_Object = MibTableColumn
tnPtpClockDefaultDSConfigIpAddress = _TnPtpClockDefaultDSConfigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 1, 1, 7),
    _TnPtpClockDefaultDSConfigIpAddress_Type()
)
tnPtpClockDefaultDSConfigIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSConfigIpAddress.setStatus("current")


class _TnPtpClockDefaultDSConfigAdminStatus_Type(Integer32):
    """Custom type tnPtpClockDefaultDSConfigAdminStatus based on Integer32"""
    defaultValue = 0


_TnPtpClockDefaultDSConfigAdminStatus_Type.__name__ = "Integer32"
_TnPtpClockDefaultDSConfigAdminStatus_Object = MibTableColumn
tnPtpClockDefaultDSConfigAdminStatus = _TnPtpClockDefaultDSConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 1, 1, 8),
    _TnPtpClockDefaultDSConfigAdminStatus_Type()
)
tnPtpClockDefaultDSConfigAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSConfigAdminStatus.setStatus("current")
_TnPtpClockDefaultDSConfigRowStatus_Type = RowStatus
_TnPtpClockDefaultDSConfigRowStatus_Object = MibTableColumn
tnPtpClockDefaultDSConfigRowStatus = _TnPtpClockDefaultDSConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 1, 1, 9),
    _TnPtpClockDefaultDSConfigRowStatus_Type()
)
tnPtpClockDefaultDSConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSConfigRowStatus.setStatus("current")


class _TnPtpClockDefaultDSConfigLocalPriority_Type(Unsigned32):
    """Custom type tnPtpClockDefaultDSConfigLocalPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TnPtpClockDefaultDSConfigLocalPriority_Type.__name__ = "Unsigned32"
_TnPtpClockDefaultDSConfigLocalPriority_Object = MibTableColumn
tnPtpClockDefaultDSConfigLocalPriority = _TnPtpClockDefaultDSConfigLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 1, 1, 10),
    _TnPtpClockDefaultDSConfigLocalPriority_Type()
)
tnPtpClockDefaultDSConfigLocalPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSConfigLocalPriority.setStatus("current")
_TnPtpClockDefaultDSInfoTable_Object = MibTable
tnPtpClockDefaultDSInfoTable = _TnPtpClockDefaultDSInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSInfoTable.setStatus("current")
_TnPtpClockDefaultDSInfoEntry_Object = MibTableRow
tnPtpClockDefaultDSInfoEntry = _TnPtpClockDefaultDSInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 2, 1)
)
tnPtpClockDefaultDSInfoEntry.setIndexNames(
    (0, "TROPIC-PTP-MIB", "tnPtpClockIndex"),
)
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSInfoEntry.setStatus("current")
_TnPtpClockDefaultDSInfoIdentifier_Type = AluWdmPtpClockIdentifier
_TnPtpClockDefaultDSInfoIdentifier_Object = MibTableColumn
tnPtpClockDefaultDSInfoIdentifier = _TnPtpClockDefaultDSInfoIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 2, 1, 1),
    _TnPtpClockDefaultDSInfoIdentifier_Type()
)
tnPtpClockDefaultDSInfoIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSInfoIdentifier.setStatus("current")
_TnPtpClockDefaultDSInfoTwoStepFlag_Type = TruthValue
_TnPtpClockDefaultDSInfoTwoStepFlag_Object = MibTableColumn
tnPtpClockDefaultDSInfoTwoStepFlag = _TnPtpClockDefaultDSInfoTwoStepFlag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 2, 1, 2),
    _TnPtpClockDefaultDSInfoTwoStepFlag_Type()
)
tnPtpClockDefaultDSInfoTwoStepFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSInfoTwoStepFlag.setStatus("current")
_TnPtpClockDefaultDSInfoNumberOfPorts_Type = Unsigned32
_TnPtpClockDefaultDSInfoNumberOfPorts_Object = MibTableColumn
tnPtpClockDefaultDSInfoNumberOfPorts = _TnPtpClockDefaultDSInfoNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 2, 1, 3),
    _TnPtpClockDefaultDSInfoNumberOfPorts_Type()
)
tnPtpClockDefaultDSInfoNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSInfoNumberOfPorts.setStatus("current")


class _TnPtpClockDefaultDSInfoClass_Type(Unsigned32):
    """Custom type tnPtpClockDefaultDSInfoClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnPtpClockDefaultDSInfoClass_Type.__name__ = "Unsigned32"
_TnPtpClockDefaultDSInfoClass_Object = MibTableColumn
tnPtpClockDefaultDSInfoClass = _TnPtpClockDefaultDSInfoClass_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 2, 1, 4),
    _TnPtpClockDefaultDSInfoClass_Type()
)
tnPtpClockDefaultDSInfoClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSInfoClass.setStatus("current")


class _TnPtpClockDefaultDSInfoAccuracy_Type(Unsigned32):
    """Custom type tnPtpClockDefaultDSInfoAccuracy based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnPtpClockDefaultDSInfoAccuracy_Type.__name__ = "Unsigned32"
_TnPtpClockDefaultDSInfoAccuracy_Object = MibTableColumn
tnPtpClockDefaultDSInfoAccuracy = _TnPtpClockDefaultDSInfoAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 2, 1, 5),
    _TnPtpClockDefaultDSInfoAccuracy_Type()
)
tnPtpClockDefaultDSInfoAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSInfoAccuracy.setStatus("current")
_TnPtpClockDefaultDSInfoOffsetScaledLogVariance_Type = Integer32
_TnPtpClockDefaultDSInfoOffsetScaledLogVariance_Object = MibTableColumn
tnPtpClockDefaultDSInfoOffsetScaledLogVariance = _TnPtpClockDefaultDSInfoOffsetScaledLogVariance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 2, 1, 6),
    _TnPtpClockDefaultDSInfoOffsetScaledLogVariance_Type()
)
tnPtpClockDefaultDSInfoOffsetScaledLogVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSInfoOffsetScaledLogVariance.setStatus("current")
_TnPtpClockCurrentDSTable_Object = MibTable
tnPtpClockCurrentDSTable = _TnPtpClockCurrentDSTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tnPtpClockCurrentDSTable.setStatus("current")
_TnPtpClockCurrentDSEntry_Object = MibTableRow
tnPtpClockCurrentDSEntry = _TnPtpClockCurrentDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 3, 1)
)
tnPtpClockCurrentDSEntry.setIndexNames(
    (0, "TROPIC-PTP-MIB", "tnPtpClockIndex"),
)
if mibBuilder.loadTexts:
    tnPtpClockCurrentDSEntry.setStatus("current")
_TnPtpClockCurrentDSOffSetFromMaster_Type = Integer32
_TnPtpClockCurrentDSOffSetFromMaster_Object = MibTableColumn
tnPtpClockCurrentDSOffSetFromMaster = _TnPtpClockCurrentDSOffSetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 3, 1, 1),
    _TnPtpClockCurrentDSOffSetFromMaster_Type()
)
tnPtpClockCurrentDSOffSetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockCurrentDSOffSetFromMaster.setStatus("current")
_TnPtpClockCurrentDSMeanPathDelay_Type = Unsigned32
_TnPtpClockCurrentDSMeanPathDelay_Object = MibTableColumn
tnPtpClockCurrentDSMeanPathDelay = _TnPtpClockCurrentDSMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 3, 1, 2),
    _TnPtpClockCurrentDSMeanPathDelay_Type()
)
tnPtpClockCurrentDSMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockCurrentDSMeanPathDelay.setStatus("current")


class _TnPtpClockCurrentDSCurrentTime_Type(OctetString):
    """Custom type tnPtpClockCurrentDSCurrentTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(81, 81),
    )
    fixed_length = 81


_TnPtpClockCurrentDSCurrentTime_Type.__name__ = "OctetString"
_TnPtpClockCurrentDSCurrentTime_Object = MibTableColumn
tnPtpClockCurrentDSCurrentTime = _TnPtpClockCurrentDSCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 3, 1, 3),
    _TnPtpClockCurrentDSCurrentTime_Type()
)
tnPtpClockCurrentDSCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockCurrentDSCurrentTime.setStatus("current")
_TnPtpClockCurrentDSRecoveredClockState_Type = AluWdmPtpRecoveredClockState
_TnPtpClockCurrentDSRecoveredClockState_Object = MibTableColumn
tnPtpClockCurrentDSRecoveredClockState = _TnPtpClockCurrentDSRecoveredClockState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 3, 1, 4),
    _TnPtpClockCurrentDSRecoveredClockState_Type()
)
tnPtpClockCurrentDSRecoveredClockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockCurrentDSRecoveredClockState.setStatus("current")
_TnPtpClockCurrentDSLockedPtpPort_Type = Integer32
_TnPtpClockCurrentDSLockedPtpPort_Object = MibTableColumn
tnPtpClockCurrentDSLockedPtpPort = _TnPtpClockCurrentDSLockedPtpPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 3, 1, 5),
    _TnPtpClockCurrentDSLockedPtpPort_Type()
)
tnPtpClockCurrentDSLockedPtpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockCurrentDSLockedPtpPort.setStatus("current")


class _TnPtpClockCurrentDSStepsRemoved_Type(Unsigned32):
    """Custom type tnPtpClockCurrentDSStepsRemoved based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnPtpClockCurrentDSStepsRemoved_Type.__name__ = "Unsigned32"
_TnPtpClockCurrentDSStepsRemoved_Object = MibTableColumn
tnPtpClockCurrentDSStepsRemoved = _TnPtpClockCurrentDSStepsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 3, 1, 6),
    _TnPtpClockCurrentDSStepsRemoved_Type()
)
tnPtpClockCurrentDSStepsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockCurrentDSStepsRemoved.setStatus("current")
_TnPtpClockParentDSTable_Object = MibTable
tnPtpClockParentDSTable = _TnPtpClockParentDSTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 4)
)
if mibBuilder.loadTexts:
    tnPtpClockParentDSTable.setStatus("current")
_TnPtpClockParentDSEntry_Object = MibTableRow
tnPtpClockParentDSEntry = _TnPtpClockParentDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 4, 1)
)
tnPtpClockParentDSEntry.setIndexNames(
    (0, "TROPIC-PTP-MIB", "tnPtpClockIndex"),
)
if mibBuilder.loadTexts:
    tnPtpClockParentDSEntry.setStatus("current")
_TnPtpClockParentDSIdentifier_Type = AluWdmPtpClockIdentifier
_TnPtpClockParentDSIdentifier_Object = MibTableColumn
tnPtpClockParentDSIdentifier = _TnPtpClockParentDSIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 4, 1, 1),
    _TnPtpClockParentDSIdentifier_Type()
)
tnPtpClockParentDSIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockParentDSIdentifier.setStatus("current")
_TnPtpClockParentDSPortNum_Type = Integer32
_TnPtpClockParentDSPortNum_Object = MibTableColumn
tnPtpClockParentDSPortNum = _TnPtpClockParentDSPortNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 4, 1, 2),
    _TnPtpClockParentDSPortNum_Type()
)
tnPtpClockParentDSPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockParentDSPortNum.setStatus("current")
_TnPtpClockParentDSStats_Type = TruthValue
_TnPtpClockParentDSStats_Object = MibTableColumn
tnPtpClockParentDSStats = _TnPtpClockParentDSStats_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 4, 1, 3),
    _TnPtpClockParentDSStats_Type()
)
tnPtpClockParentDSStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockParentDSStats.setStatus("current")
_TnPtpClockParentDSOffsetScaledLogVariance_Type = Integer32
_TnPtpClockParentDSOffsetScaledLogVariance_Object = MibTableColumn
tnPtpClockParentDSOffsetScaledLogVariance = _TnPtpClockParentDSOffsetScaledLogVariance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 4, 1, 4),
    _TnPtpClockParentDSOffsetScaledLogVariance_Type()
)
tnPtpClockParentDSOffsetScaledLogVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockParentDSOffsetScaledLogVariance.setStatus("current")
_TnPtpClockParentDSPhaseChangeRate_Type = Integer32
_TnPtpClockParentDSPhaseChangeRate_Object = MibTableColumn
tnPtpClockParentDSPhaseChangeRate = _TnPtpClockParentDSPhaseChangeRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 4, 1, 5),
    _TnPtpClockParentDSPhaseChangeRate_Type()
)
tnPtpClockParentDSPhaseChangeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockParentDSPhaseChangeRate.setStatus("current")
_TnPtpClockParentDSGrandmasterClockId_Type = AluWdmPtpClockIdentifier
_TnPtpClockParentDSGrandmasterClockId_Object = MibTableColumn
tnPtpClockParentDSGrandmasterClockId = _TnPtpClockParentDSGrandmasterClockId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 4, 1, 6),
    _TnPtpClockParentDSGrandmasterClockId_Type()
)
tnPtpClockParentDSGrandmasterClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockParentDSGrandmasterClockId.setStatus("current")


class _TnPtpClockParentDSGrandmasterClass_Type(Unsigned32):
    """Custom type tnPtpClockParentDSGrandmasterClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnPtpClockParentDSGrandmasterClass_Type.__name__ = "Unsigned32"
_TnPtpClockParentDSGrandmasterClass_Object = MibTableColumn
tnPtpClockParentDSGrandmasterClass = _TnPtpClockParentDSGrandmasterClass_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 4, 1, 7),
    _TnPtpClockParentDSGrandmasterClass_Type()
)
tnPtpClockParentDSGrandmasterClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockParentDSGrandmasterClass.setStatus("current")


class _TnPtpClockParentDSGrandmasterAccuracy_Type(Unsigned32):
    """Custom type tnPtpClockParentDSGrandmasterAccuracy based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnPtpClockParentDSGrandmasterAccuracy_Type.__name__ = "Unsigned32"
_TnPtpClockParentDSGrandmasterAccuracy_Object = MibTableColumn
tnPtpClockParentDSGrandmasterAccuracy = _TnPtpClockParentDSGrandmasterAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 4, 1, 8),
    _TnPtpClockParentDSGrandmasterAccuracy_Type()
)
tnPtpClockParentDSGrandmasterAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockParentDSGrandmasterAccuracy.setStatus("current")
_TnPtpClockParentDSGrandmasterOffsetScaledLogVariance_Type = Unsigned32
_TnPtpClockParentDSGrandmasterOffsetScaledLogVariance_Object = MibTableColumn
tnPtpClockParentDSGrandmasterOffsetScaledLogVariance = _TnPtpClockParentDSGrandmasterOffsetScaledLogVariance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 4, 1, 9),
    _TnPtpClockParentDSGrandmasterOffsetScaledLogVariance_Type()
)
tnPtpClockParentDSGrandmasterOffsetScaledLogVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockParentDSGrandmasterOffsetScaledLogVariance.setStatus("current")


class _TnPtpClockParentDSGrandmasterPriority1_Type(Unsigned32):
    """Custom type tnPtpClockParentDSGrandmasterPriority1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnPtpClockParentDSGrandmasterPriority1_Type.__name__ = "Unsigned32"
_TnPtpClockParentDSGrandmasterPriority1_Object = MibTableColumn
tnPtpClockParentDSGrandmasterPriority1 = _TnPtpClockParentDSGrandmasterPriority1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 4, 1, 10),
    _TnPtpClockParentDSGrandmasterPriority1_Type()
)
tnPtpClockParentDSGrandmasterPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockParentDSGrandmasterPriority1.setStatus("current")


class _TnPtpClockParentDSGrandmasterPriority2_Type(Unsigned32):
    """Custom type tnPtpClockParentDSGrandmasterPriority2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnPtpClockParentDSGrandmasterPriority2_Type.__name__ = "Unsigned32"
_TnPtpClockParentDSGrandmasterPriority2_Object = MibTableColumn
tnPtpClockParentDSGrandmasterPriority2 = _TnPtpClockParentDSGrandmasterPriority2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 4, 1, 11),
    _TnPtpClockParentDSGrandmasterPriority2_Type()
)
tnPtpClockParentDSGrandmasterPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockParentDSGrandmasterPriority2.setStatus("current")
_TnPtpClockTimePropertiesDSTable_Object = MibTable
tnPtpClockTimePropertiesDSTable = _TnPtpClockTimePropertiesDSTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 5)
)
if mibBuilder.loadTexts:
    tnPtpClockTimePropertiesDSTable.setStatus("current")
_TnPtpClockTimePropertiesDSEntry_Object = MibTableRow
tnPtpClockTimePropertiesDSEntry = _TnPtpClockTimePropertiesDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 5, 1)
)
tnPtpClockTimePropertiesDSEntry.setIndexNames(
    (0, "TROPIC-PTP-MIB", "tnPtpClockIndex"),
)
if mibBuilder.loadTexts:
    tnPtpClockTimePropertiesDSEntry.setStatus("current")
_TnPtpClockTimePropertiesDSCurrentUtcOffset_Type = Integer32
_TnPtpClockTimePropertiesDSCurrentUtcOffset_Object = MibTableColumn
tnPtpClockTimePropertiesDSCurrentUtcOffset = _TnPtpClockTimePropertiesDSCurrentUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 5, 1, 1),
    _TnPtpClockTimePropertiesDSCurrentUtcOffset_Type()
)
tnPtpClockTimePropertiesDSCurrentUtcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockTimePropertiesDSCurrentUtcOffset.setStatus("current")
_TnPtpClockTimePropertiesDSCurrentUtcOffsetValid_Type = TruthValue
_TnPtpClockTimePropertiesDSCurrentUtcOffsetValid_Object = MibTableColumn
tnPtpClockTimePropertiesDSCurrentUtcOffsetValid = _TnPtpClockTimePropertiesDSCurrentUtcOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 5, 1, 2),
    _TnPtpClockTimePropertiesDSCurrentUtcOffsetValid_Type()
)
tnPtpClockTimePropertiesDSCurrentUtcOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockTimePropertiesDSCurrentUtcOffsetValid.setStatus("current")
_TnPtpClockTimePropertiesDSLeap59_Type = TruthValue
_TnPtpClockTimePropertiesDSLeap59_Object = MibTableColumn
tnPtpClockTimePropertiesDSLeap59 = _TnPtpClockTimePropertiesDSLeap59_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 5, 1, 3),
    _TnPtpClockTimePropertiesDSLeap59_Type()
)
tnPtpClockTimePropertiesDSLeap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockTimePropertiesDSLeap59.setStatus("current")
_TnPtpClockTimePropertiesDSLeap61_Type = TruthValue
_TnPtpClockTimePropertiesDSLeap61_Object = MibTableColumn
tnPtpClockTimePropertiesDSLeap61 = _TnPtpClockTimePropertiesDSLeap61_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 5, 1, 4),
    _TnPtpClockTimePropertiesDSLeap61_Type()
)
tnPtpClockTimePropertiesDSLeap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockTimePropertiesDSLeap61.setStatus("current")
_TnPtpClockTimePropertiesDSTimeTraceable_Type = TruthValue
_TnPtpClockTimePropertiesDSTimeTraceable_Object = MibTableColumn
tnPtpClockTimePropertiesDSTimeTraceable = _TnPtpClockTimePropertiesDSTimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 5, 1, 5),
    _TnPtpClockTimePropertiesDSTimeTraceable_Type()
)
tnPtpClockTimePropertiesDSTimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockTimePropertiesDSTimeTraceable.setStatus("current")
_TnPtpClockTimePropertiesDSFrequencyTraceable_Type = TruthValue
_TnPtpClockTimePropertiesDSFrequencyTraceable_Object = MibTableColumn
tnPtpClockTimePropertiesDSFrequencyTraceable = _TnPtpClockTimePropertiesDSFrequencyTraceable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 5, 1, 6),
    _TnPtpClockTimePropertiesDSFrequencyTraceable_Type()
)
tnPtpClockTimePropertiesDSFrequencyTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockTimePropertiesDSFrequencyTraceable.setStatus("current")
_TnPtpClockTimePropertiesDSPtpTimescale_Type = TruthValue
_TnPtpClockTimePropertiesDSPtpTimescale_Object = MibTableColumn
tnPtpClockTimePropertiesDSPtpTimescale = _TnPtpClockTimePropertiesDSPtpTimescale_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 5, 1, 7),
    _TnPtpClockTimePropertiesDSPtpTimescale_Type()
)
tnPtpClockTimePropertiesDSPtpTimescale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockTimePropertiesDSPtpTimescale.setStatus("current")


class _TnPtpClockTimePropertiesDSPtpTimeSource_Type(Unsigned32):
    """Custom type tnPtpClockTimePropertiesDSPtpTimeSource based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnPtpClockTimePropertiesDSPtpTimeSource_Type.__name__ = "Unsigned32"
_TnPtpClockTimePropertiesDSPtpTimeSource_Object = MibTableColumn
tnPtpClockTimePropertiesDSPtpTimeSource = _TnPtpClockTimePropertiesDSPtpTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 2, 5, 1, 8),
    _TnPtpClockTimePropertiesDSPtpTimeSource_Type()
)
tnPtpClockTimePropertiesDSPtpTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpClockTimePropertiesDSPtpTimeSource.setStatus("current")
_TnPtpPort_ObjectIdentity = ObjectIdentity
tnPtpPort = _TnPtpPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3)
)
_TnPtpPortNextIndexTable_Object = MibTable
tnPtpPortNextIndexTable = _TnPtpPortNextIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tnPtpPortNextIndexTable.setStatus("current")
_TnPtpPortNextIndexEntry_Object = MibTableRow
tnPtpPortNextIndexEntry = _TnPtpPortNextIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 1, 1)
)
tnPtpPortNextIndexEntry.setIndexNames(
    (0, "TROPIC-PTP-MIB", "tnPtpClockIndex"),
)
if mibBuilder.loadTexts:
    tnPtpPortNextIndexEntry.setStatus("current")
_TnPtpPortNextIndex_Type = Integer32
_TnPtpPortNextIndex_Object = MibTableColumn
tnPtpPortNextIndex = _TnPtpPortNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 1, 1, 1),
    _TnPtpPortNextIndex_Type()
)
tnPtpPortNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortNextIndex.setStatus("current")
_TnPtpPortDSConfigTable_Object = MibTable
tnPtpPortDSConfigTable = _TnPtpPortDSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tnPtpPortDSConfigTable.setStatus("current")
_TnPtpPortDSConfigEntry_Object = MibTableRow
tnPtpPortDSConfigEntry = _TnPtpPortDSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1)
)
tnPtpPortDSConfigEntry.setIndexNames(
    (0, "TROPIC-PTP-MIB", "tnPtpClockIndex"),
    (0, "TROPIC-PTP-MIB", "tnPtpPortDSPortIndex"),
)
if mibBuilder.loadTexts:
    tnPtpPortDSConfigEntry.setStatus("current")


class _TnPtpPortDSPortIndex_Type(Integer32):
    """Custom type tnPtpPortDSPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_TnPtpPortDSPortIndex_Type.__name__ = "Integer32"
_TnPtpPortDSPortIndex_Object = MibTableColumn
tnPtpPortDSPortIndex = _TnPtpPortDSPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 1),
    _TnPtpPortDSPortIndex_Type()
)
tnPtpPortDSPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPtpPortDSPortIndex.setStatus("current")
_TnPtpPortDSConfigAssociatedPhysicalPort_Type = InterfaceIndex
_TnPtpPortDSConfigAssociatedPhysicalPort_Object = MibTableColumn
tnPtpPortDSConfigAssociatedPhysicalPort = _TnPtpPortDSConfigAssociatedPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 2),
    _TnPtpPortDSConfigAssociatedPhysicalPort_Type()
)
tnPtpPortDSConfigAssociatedPhysicalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigAssociatedPhysicalPort.setStatus("current")


class _TnPtpPortDSConfigVlanVID_Type(Unsigned32):
    """Custom type tnPtpPortDSConfigVlanVID based on Unsigned32"""
    defaultValue = 0


_TnPtpPortDSConfigVlanVID_Type.__name__ = "Unsigned32"
_TnPtpPortDSConfigVlanVID_Object = MibTableColumn
tnPtpPortDSConfigVlanVID = _TnPtpPortDSConfigVlanVID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 3),
    _TnPtpPortDSConfigVlanVID_Type()
)
tnPtpPortDSConfigVlanVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigVlanVID.setStatus("current")


class _TnPtpPortDSConfigVlanTPID_Type(Unsigned32):
    """Custom type tnPtpPortDSConfigVlanTPID based on Unsigned32"""
    defaultValue = 33024


_TnPtpPortDSConfigVlanTPID_Type.__name__ = "Unsigned32"
_TnPtpPortDSConfigVlanTPID_Object = MibTableColumn
tnPtpPortDSConfigVlanTPID = _TnPtpPortDSConfigVlanTPID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 4),
    _TnPtpPortDSConfigVlanTPID_Type()
)
tnPtpPortDSConfigVlanTPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigVlanTPID.setStatus("current")


class _TnPtpPortDSConfigAnnoRxTimeout_Type(Integer32):
    """Custom type tnPtpPortDSConfigAnnoRxTimeout based on Integer32"""
    defaultValue = 3


_TnPtpPortDSConfigAnnoRxTimeout_Type.__name__ = "Integer32"
_TnPtpPortDSConfigAnnoRxTimeout_Object = MibTableColumn
tnPtpPortDSConfigAnnoRxTimeout = _TnPtpPortDSConfigAnnoRxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 5),
    _TnPtpPortDSConfigAnnoRxTimeout_Type()
)
tnPtpPortDSConfigAnnoRxTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigAnnoRxTimeout.setStatus("current")


class _TnPtpPortDSConfigLogAnnoInterval_Type(Integer32):
    """Custom type tnPtpPortDSConfigLogAnnoInterval based on Integer32"""
    defaultValue = 0


_TnPtpPortDSConfigLogAnnoInterval_Type.__name__ = "Integer32"
_TnPtpPortDSConfigLogAnnoInterval_Object = MibTableColumn
tnPtpPortDSConfigLogAnnoInterval = _TnPtpPortDSConfigLogAnnoInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 6),
    _TnPtpPortDSConfigLogAnnoInterval_Type()
)
tnPtpPortDSConfigLogAnnoInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigLogAnnoInterval.setStatus("current")


class _TnPtpPortDSConfigLogSyncInterval_Type(Integer32):
    """Custom type tnPtpPortDSConfigLogSyncInterval based on Integer32"""
    defaultValue = -7


_TnPtpPortDSConfigLogSyncInterval_Type.__name__ = "Integer32"
_TnPtpPortDSConfigLogSyncInterval_Object = MibTableColumn
tnPtpPortDSConfigLogSyncInterval = _TnPtpPortDSConfigLogSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 7),
    _TnPtpPortDSConfigLogSyncInterval_Type()
)
tnPtpPortDSConfigLogSyncInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigLogSyncInterval.setStatus("current")


class _TnPtpPortDSConfigLogDelayReqInterval_Type(Integer32):
    """Custom type tnPtpPortDSConfigLogDelayReqInterval based on Integer32"""
    defaultValue = -4


_TnPtpPortDSConfigLogDelayReqInterval_Type.__name__ = "Integer32"
_TnPtpPortDSConfigLogDelayReqInterval_Object = MibTableColumn
tnPtpPortDSConfigLogDelayReqInterval = _TnPtpPortDSConfigLogDelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 8),
    _TnPtpPortDSConfigLogDelayReqInterval_Type()
)
tnPtpPortDSConfigLogDelayReqInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigLogDelayReqInterval.setStatus("current")


class _TnPtpPortDSConfigLogMinPDelayReqInterval_Type(Integer32):
    """Custom type tnPtpPortDSConfigLogMinPDelayReqInterval based on Integer32"""
    defaultValue = -4


_TnPtpPortDSConfigLogMinPDelayReqInterval_Type.__name__ = "Integer32"
_TnPtpPortDSConfigLogMinPDelayReqInterval_Object = MibTableColumn
tnPtpPortDSConfigLogMinPDelayReqInterval = _TnPtpPortDSConfigLogMinPDelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 9),
    _TnPtpPortDSConfigLogMinPDelayReqInterval_Type()
)
tnPtpPortDSConfigLogMinPDelayReqInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigLogMinPDelayReqInterval.setStatus("current")


class _TnPtpPortDSConfigAdminStatus_Type(Integer32):
    """Custom type tnPtpPortDSConfigAdminStatus based on Integer32"""
    defaultValue = 0


_TnPtpPortDSConfigAdminStatus_Type.__name__ = "Integer32"
_TnPtpPortDSConfigAdminStatus_Object = MibTableColumn
tnPtpPortDSConfigAdminStatus = _TnPtpPortDSConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 10),
    _TnPtpPortDSConfigAdminStatus_Type()
)
tnPtpPortDSConfigAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigAdminStatus.setStatus("current")


class _TnPtpPortDSConfigRole_Type(Integer32):
    """Custom type tnPtpPortDSConfigRole based on Integer32"""
    defaultValue = 0


_TnPtpPortDSConfigRole_Type.__name__ = "Integer32"
_TnPtpPortDSConfigRole_Object = MibTableColumn
tnPtpPortDSConfigRole = _TnPtpPortDSConfigRole_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 11),
    _TnPtpPortDSConfigRole_Type()
)
tnPtpPortDSConfigRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigRole.setStatus("current")


class _TnPtpPortDSConfigDelayMechanism_Type(Integer32):
    """Custom type tnPtpPortDSConfigDelayMechanism based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e2e", 1),
          ("p2p", 2))
    )


_TnPtpPortDSConfigDelayMechanism_Type.__name__ = "Integer32"
_TnPtpPortDSConfigDelayMechanism_Object = MibTableColumn
tnPtpPortDSConfigDelayMechanism = _TnPtpPortDSConfigDelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 12),
    _TnPtpPortDSConfigDelayMechanism_Type()
)
tnPtpPortDSConfigDelayMechanism.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigDelayMechanism.setStatus("current")


class _TnPtpPortDSConfigVersionNumber_Type(Integer32):
    """Custom type tnPtpPortDSConfigVersionNumber based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_TnPtpPortDSConfigVersionNumber_Type.__name__ = "Integer32"
_TnPtpPortDSConfigVersionNumber_Object = MibTableColumn
tnPtpPortDSConfigVersionNumber = _TnPtpPortDSConfigVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 13),
    _TnPtpPortDSConfigVersionNumber_Type()
)
tnPtpPortDSConfigVersionNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigVersionNumber.setStatus("current")
_TnPtpPortDSConfigAsymCorrection_Type = Integer32
_TnPtpPortDSConfigAsymCorrection_Object = MibTableColumn
tnPtpPortDSConfigAsymCorrection = _TnPtpPortDSConfigAsymCorrection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 14),
    _TnPtpPortDSConfigAsymCorrection_Type()
)
tnPtpPortDSConfigAsymCorrection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigAsymCorrection.setStatus("current")


class _TnPtpPortDSConfigTwoStepFlag_Type(TruthValue):
    """Custom type tnPtpPortDSConfigTwoStepFlag based on TruthValue"""
    defaultValue = 2


_TnPtpPortDSConfigTwoStepFlag_Type.__name__ = "TruthValue"
_TnPtpPortDSConfigTwoStepFlag_Object = MibTableColumn
tnPtpPortDSConfigTwoStepFlag = _TnPtpPortDSConfigTwoStepFlag_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 15),
    _TnPtpPortDSConfigTwoStepFlag_Type()
)
tnPtpPortDSConfigTwoStepFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigTwoStepFlag.setStatus("current")


class _TnPtpPortDSConfigEncapType_Type(Unsigned32):
    """Custom type tnPtpPortDSConfigEncapType based on Unsigned32"""
    defaultValue = 3


_TnPtpPortDSConfigEncapType_Type.__name__ = "Unsigned32"
_TnPtpPortDSConfigEncapType_Object = MibTableColumn
tnPtpPortDSConfigEncapType = _TnPtpPortDSConfigEncapType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 16),
    _TnPtpPortDSConfigEncapType_Type()
)
tnPtpPortDSConfigEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigEncapType.setStatus("current")


class _TnPtpPortDSConfigAddressingMode_Type(Integer32):
    """Custom type tnPtpPortDSConfigAddressingMode based on Integer32"""
    defaultValue = 0


_TnPtpPortDSConfigAddressingMode_Type.__name__ = "Integer32"
_TnPtpPortDSConfigAddressingMode_Object = MibTableColumn
tnPtpPortDSConfigAddressingMode = _TnPtpPortDSConfigAddressingMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 17),
    _TnPtpPortDSConfigAddressingMode_Type()
)
tnPtpPortDSConfigAddressingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigAddressingMode.setStatus("current")


class _TnPtpPortDSConfigUnicastForDelayReq_Type(TruthValue):
    """Custom type tnPtpPortDSConfigUnicastForDelayReq based on TruthValue"""
    defaultValue = 2


_TnPtpPortDSConfigUnicastForDelayReq_Type.__name__ = "TruthValue"
_TnPtpPortDSConfigUnicastForDelayReq_Object = MibTableColumn
tnPtpPortDSConfigUnicastForDelayReq = _TnPtpPortDSConfigUnicastForDelayReq_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 18),
    _TnPtpPortDSConfigUnicastForDelayReq_Type()
)
tnPtpPortDSConfigUnicastForDelayReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigUnicastForDelayReq.setStatus("deprecated")


class _TnPtpPortDSConfigUnicastNegotiation_Type(TruthValue):
    """Custom type tnPtpPortDSConfigUnicastNegotiation based on TruthValue"""
    defaultValue = 2


_TnPtpPortDSConfigUnicastNegotiation_Type.__name__ = "TruthValue"
_TnPtpPortDSConfigUnicastNegotiation_Object = MibTableColumn
tnPtpPortDSConfigUnicastNegotiation = _TnPtpPortDSConfigUnicastNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 19),
    _TnPtpPortDSConfigUnicastNegotiation_Type()
)
tnPtpPortDSConfigUnicastNegotiation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigUnicastNegotiation.setStatus("current")
_TnPtpPortDSConfigDestMac_Type = MacAddress
_TnPtpPortDSConfigDestMac_Object = MibTableColumn
tnPtpPortDSConfigDestMac = _TnPtpPortDSConfigDestMac_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 20),
    _TnPtpPortDSConfigDestMac_Type()
)
tnPtpPortDSConfigDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigDestMac.setStatus("current")


class _TnPtpPortDSConfigDestIpAddrType_Type(InetAddressType):
    """Custom type tnPtpPortDSConfigDestIpAddrType based on InetAddressType"""
    defaultValue = 1


_TnPtpPortDSConfigDestIpAddrType_Type.__name__ = "InetAddressType"
_TnPtpPortDSConfigDestIpAddrType_Object = MibTableColumn
tnPtpPortDSConfigDestIpAddrType = _TnPtpPortDSConfigDestIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 21),
    _TnPtpPortDSConfigDestIpAddrType_Type()
)
tnPtpPortDSConfigDestIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigDestIpAddrType.setStatus("current")
_TnPtpPortDSConfigDestIpAddr_Type = InetAddress
_TnPtpPortDSConfigDestIpAddr_Object = MibTableColumn
tnPtpPortDSConfigDestIpAddr = _TnPtpPortDSConfigDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 22),
    _TnPtpPortDSConfigDestIpAddr_Type()
)
tnPtpPortDSConfigDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigDestIpAddr.setStatus("current")
_TnPtpPortDSConfigRowStatus_Type = RowStatus
_TnPtpPortDSConfigRowStatus_Object = MibTableColumn
tnPtpPortDSConfigRowStatus = _TnPtpPortDSConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 23),
    _TnPtpPortDSConfigRowStatus_Type()
)
tnPtpPortDSConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigRowStatus.setStatus("current")
_TnPtpPortDSConfigConnectedPtpioTimingPort_Type = InterfaceIndexOrZero
_TnPtpPortDSConfigConnectedPtpioTimingPort_Object = MibTableColumn
tnPtpPortDSConfigConnectedPtpioTimingPort = _TnPtpPortDSConfigConnectedPtpioTimingPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 24),
    _TnPtpPortDSConfigConnectedPtpioTimingPort_Type()
)
tnPtpPortDSConfigConnectedPtpioTimingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigConnectedPtpioTimingPort.setStatus("current")


class _TnPtpPortDSConfigAutoLinkAsyMeasureTrigger_Type(TruthValue):
    """Custom type tnPtpPortDSConfigAutoLinkAsyMeasureTrigger based on TruthValue"""
    defaultValue = 2


_TnPtpPortDSConfigAutoLinkAsyMeasureTrigger_Type.__name__ = "TruthValue"
_TnPtpPortDSConfigAutoLinkAsyMeasureTrigger_Object = MibTableColumn
tnPtpPortDSConfigAutoLinkAsyMeasureTrigger = _TnPtpPortDSConfigAutoLinkAsyMeasureTrigger_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 25),
    _TnPtpPortDSConfigAutoLinkAsyMeasureTrigger_Type()
)
tnPtpPortDSConfigAutoLinkAsyMeasureTrigger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigAutoLinkAsyMeasureTrigger.setStatus("current")


class _TnPtpPortDSConfigNotSlave_Type(TruthValue):
    """Custom type tnPtpPortDSConfigNotSlave based on TruthValue"""
    defaultValue = 2


_TnPtpPortDSConfigNotSlave_Type.__name__ = "TruthValue"
_TnPtpPortDSConfigNotSlave_Object = MibTableColumn
tnPtpPortDSConfigNotSlave = _TnPtpPortDSConfigNotSlave_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 26),
    _TnPtpPortDSConfigNotSlave_Type()
)
tnPtpPortDSConfigNotSlave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigNotSlave.setStatus("current")


class _TnPtpPortDSConfigLocalPriority_Type(Unsigned32):
    """Custom type tnPtpPortDSConfigLocalPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TnPtpPortDSConfigLocalPriority_Type.__name__ = "Unsigned32"
_TnPtpPortDSConfigLocalPriority_Object = MibTableColumn
tnPtpPortDSConfigLocalPriority = _TnPtpPortDSConfigLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 2, 1, 27),
    _TnPtpPortDSConfigLocalPriority_Type()
)
tnPtpPortDSConfigLocalPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpPortDSConfigLocalPriority.setStatus("current")
_TnPtpPortDSInfoTable_Object = MibTable
tnPtpPortDSInfoTable = _TnPtpPortDSInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tnPtpPortDSInfoTable.setStatus("current")
_TnPtpPortDSInfoEntry_Object = MibTableRow
tnPtpPortDSInfoEntry = _TnPtpPortDSInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1)
)
tnPtpPortDSInfoEntry.setIndexNames(
    (0, "TROPIC-PTP-MIB", "tnPtpClockIndex"),
    (0, "TROPIC-PTP-MIB", "tnPtpPortDSPortIndex"),
)
if mibBuilder.loadTexts:
    tnPtpPortDSInfoEntry.setStatus("current")
_TnPtpPortDSInfoPeerPathDelay_Type = Integer32
_TnPtpPortDSInfoPeerPathDelay_Object = MibTableColumn
tnPtpPortDSInfoPeerPathDelay = _TnPtpPortDSInfoPeerPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1, 1),
    _TnPtpPortDSInfoPeerPathDelay_Type()
)
tnPtpPortDSInfoPeerPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortDSInfoPeerPathDelay.setStatus("current")
_TnPtpPortDSInfoPortOperState_Type = AluWdmtnPtpPortState
_TnPtpPortDSInfoPortOperState_Object = MibTableColumn
tnPtpPortDSInfoPortOperState = _TnPtpPortDSInfoPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1, 2),
    _TnPtpPortDSInfoPortOperState_Type()
)
tnPtpPortDSInfoPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortDSInfoPortOperState.setStatus("current")
_TnPtpPortDSInfoNumOfSessions_Type = Integer32
_TnPtpPortDSInfoNumOfSessions_Object = MibTableColumn
tnPtpPortDSInfoNumOfSessions = _TnPtpPortDSInfoNumOfSessions_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1, 3),
    _TnPtpPortDSInfoNumOfSessions_Type()
)
tnPtpPortDSInfoNumOfSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortDSInfoNumOfSessions.setStatus("deprecated")
_TnPtpPortDSInfoAutoLinkAsyMeasureStatus_Type = Integer32
_TnPtpPortDSInfoAutoLinkAsyMeasureStatus_Object = MibTableColumn
tnPtpPortDSInfoAutoLinkAsyMeasureStatus = _TnPtpPortDSInfoAutoLinkAsyMeasureStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1, 4),
    _TnPtpPortDSInfoAutoLinkAsyMeasureStatus_Type()
)
tnPtpPortDSInfoAutoLinkAsyMeasureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortDSInfoAutoLinkAsyMeasureStatus.setStatus("current")
_TnPtpPortDSInfoMeasuredLinkAsymmetry_Type = Integer32
_TnPtpPortDSInfoMeasuredLinkAsymmetry_Object = MibTableColumn
tnPtpPortDSInfoMeasuredLinkAsymmetry = _TnPtpPortDSInfoMeasuredLinkAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1, 5),
    _TnPtpPortDSInfoMeasuredLinkAsymmetry_Type()
)
tnPtpPortDSInfoMeasuredLinkAsymmetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortDSInfoMeasuredLinkAsymmetry.setStatus("current")
_TnPtpPortDSInfoAnnounceMsgTx_Type = Counter64
_TnPtpPortDSInfoAnnounceMsgTx_Object = MibTableColumn
tnPtpPortDSInfoAnnounceMsgTx = _TnPtpPortDSInfoAnnounceMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1, 6),
    _TnPtpPortDSInfoAnnounceMsgTx_Type()
)
tnPtpPortDSInfoAnnounceMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortDSInfoAnnounceMsgTx.setStatus("current")
_TnPtpPortDSInfoAnnounceMsgRx_Type = Counter64
_TnPtpPortDSInfoAnnounceMsgRx_Object = MibTableColumn
tnPtpPortDSInfoAnnounceMsgRx = _TnPtpPortDSInfoAnnounceMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1, 7),
    _TnPtpPortDSInfoAnnounceMsgRx_Type()
)
tnPtpPortDSInfoAnnounceMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortDSInfoAnnounceMsgRx.setStatus("current")
_TnPtpPortDSInfoSyncMsgTx_Type = Counter64
_TnPtpPortDSInfoSyncMsgTx_Object = MibTableColumn
tnPtpPortDSInfoSyncMsgTx = _TnPtpPortDSInfoSyncMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1, 8),
    _TnPtpPortDSInfoSyncMsgTx_Type()
)
tnPtpPortDSInfoSyncMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortDSInfoSyncMsgTx.setStatus("current")
_TnPtpPortDSInfoSyncMsgRx_Type = Counter64
_TnPtpPortDSInfoSyncMsgRx_Object = MibTableColumn
tnPtpPortDSInfoSyncMsgRx = _TnPtpPortDSInfoSyncMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1, 9),
    _TnPtpPortDSInfoSyncMsgRx_Type()
)
tnPtpPortDSInfoSyncMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortDSInfoSyncMsgRx.setStatus("current")
_TnPtpPortDSInfoDelayReqMsgTx_Type = Counter64
_TnPtpPortDSInfoDelayReqMsgTx_Object = MibTableColumn
tnPtpPortDSInfoDelayReqMsgTx = _TnPtpPortDSInfoDelayReqMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1, 10),
    _TnPtpPortDSInfoDelayReqMsgTx_Type()
)
tnPtpPortDSInfoDelayReqMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortDSInfoDelayReqMsgTx.setStatus("current")
_TnPtpPortDSInfoDelayReqMsgRx_Type = Counter64
_TnPtpPortDSInfoDelayReqMsgRx_Object = MibTableColumn
tnPtpPortDSInfoDelayReqMsgRx = _TnPtpPortDSInfoDelayReqMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1, 11),
    _TnPtpPortDSInfoDelayReqMsgRx_Type()
)
tnPtpPortDSInfoDelayReqMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortDSInfoDelayReqMsgRx.setStatus("current")
_TnPtpPortDSInfoDelayRspMsgTx_Type = Counter64
_TnPtpPortDSInfoDelayRspMsgTx_Object = MibTableColumn
tnPtpPortDSInfoDelayRspMsgTx = _TnPtpPortDSInfoDelayRspMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1, 12),
    _TnPtpPortDSInfoDelayRspMsgTx_Type()
)
tnPtpPortDSInfoDelayRspMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortDSInfoDelayRspMsgTx.setStatus("current")
_TnPtpPortDSInfoDelayRspMsgRx_Type = Counter64
_TnPtpPortDSInfoDelayRspMsgRx_Object = MibTableColumn
tnPtpPortDSInfoDelayRspMsgRx = _TnPtpPortDSInfoDelayRspMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1, 13),
    _TnPtpPortDSInfoDelayRspMsgRx_Type()
)
tnPtpPortDSInfoDelayRspMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortDSInfoDelayRspMsgRx.setStatus("current")
_TnPtpPortDSInfoSignalingMsgTx_Type = Counter64
_TnPtpPortDSInfoSignalingMsgTx_Object = MibTableColumn
tnPtpPortDSInfoSignalingMsgTx = _TnPtpPortDSInfoSignalingMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1, 14),
    _TnPtpPortDSInfoSignalingMsgTx_Type()
)
tnPtpPortDSInfoSignalingMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortDSInfoSignalingMsgTx.setStatus("current")
_TnPtpPortDSInfoSignalingMsgRx_Type = Counter64
_TnPtpPortDSInfoSignalingMsgRx_Object = MibTableColumn
tnPtpPortDSInfoSignalingMsgRx = _TnPtpPortDSInfoSignalingMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1, 15),
    _TnPtpPortDSInfoSignalingMsgRx_Type()
)
tnPtpPortDSInfoSignalingMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortDSInfoSignalingMsgRx.setStatus("current")
_TnPtpPortDSInfoManagementMsgTx_Type = Counter64
_TnPtpPortDSInfoManagementMsgTx_Object = MibTableColumn
tnPtpPortDSInfoManagementMsgTx = _TnPtpPortDSInfoManagementMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1, 16),
    _TnPtpPortDSInfoManagementMsgTx_Type()
)
tnPtpPortDSInfoManagementMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortDSInfoManagementMsgTx.setStatus("current")
_TnPtpPortDSInfoManagementMsgRx_Type = Counter64
_TnPtpPortDSInfoManagementMsgRx_Object = MibTableColumn
tnPtpPortDSInfoManagementMsgRx = _TnPtpPortDSInfoManagementMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1, 17),
    _TnPtpPortDSInfoManagementMsgRx_Type()
)
tnPtpPortDSInfoManagementMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortDSInfoManagementMsgRx.setStatus("current")
_TnPtpPortDSInfoFollowUpMsgTx_Type = Counter64
_TnPtpPortDSInfoFollowUpMsgTx_Object = MibTableColumn
tnPtpPortDSInfoFollowUpMsgTx = _TnPtpPortDSInfoFollowUpMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1, 18),
    _TnPtpPortDSInfoFollowUpMsgTx_Type()
)
tnPtpPortDSInfoFollowUpMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortDSInfoFollowUpMsgTx.setStatus("current")
_TnPtpPortDSInfoFollowUpMsgRx_Type = Counter64
_TnPtpPortDSInfoFollowUpMsgRx_Object = MibTableColumn
tnPtpPortDSInfoFollowUpMsgRx = _TnPtpPortDSInfoFollowUpMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 3, 3, 1, 19),
    _TnPtpPortDSInfoFollowUpMsgRx_Type()
)
tnPtpPortDSInfoFollowUpMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpPortDSInfoFollowUpMsgRx.setStatus("current")
_TnPtpExtTodIf_ObjectIdentity = ObjectIdentity
tnPtpExtTodIf = _TnPtpExtTodIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 4)
)
_TnPtpExtTodIfTable_Object = MibTable
tnPtpExtTodIfTable = _TnPtpExtTodIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tnPtpExtTodIfTable.setStatus("current")
_TnPtpExtTodIfEntry_Object = MibTableRow
tnPtpExtTodIfEntry = _TnPtpExtTodIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 4, 1, 1)
)
tnPtpExtTodIfEntry.setIndexNames(
    (0, "TROPIC-PTP-MIB", "tnPtpExtTodIfIndex"),
)
if mibBuilder.loadTexts:
    tnPtpExtTodIfEntry.setStatus("current")
_TnPtpExtTodIfIndex_Type = InterfaceIndex
_TnPtpExtTodIfIndex_Object = MibTableColumn
tnPtpExtTodIfIndex = _TnPtpExtTodIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 4, 1, 1, 1),
    _TnPtpExtTodIfIndex_Type()
)
tnPtpExtTodIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPtpExtTodIfIndex.setStatus("current")


class _TnPtpExtTodIfDirection_Type(Unsigned32):
    """Custom type tnPtpExtTodIfDirection based on Unsigned32"""
    defaultValue = 0


_TnPtpExtTodIfDirection_Type.__name__ = "Unsigned32"
_TnPtpExtTodIfDirection_Object = MibTableColumn
tnPtpExtTodIfDirection = _TnPtpExtTodIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 4, 1, 1, 2),
    _TnPtpExtTodIfDirection_Type()
)
tnPtpExtTodIfDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpExtTodIfDirection.setStatus("current")


class _TnPtpExtTodSignalValid_Type(TruthValue):
    """Custom type tnPtpExtTodSignalValid based on TruthValue"""
    defaultValue = 1


_TnPtpExtTodSignalValid_Type.__name__ = "TruthValue"
_TnPtpExtTodSignalValid_Object = MibTableColumn
tnPtpExtTodSignalValid = _TnPtpExtTodSignalValid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 4, 1, 1, 3),
    _TnPtpExtTodSignalValid_Type()
)
tnPtpExtTodSignalValid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpExtTodSignalValid.setStatus("current")


class _TnPtpExtTodIfPulseFormat_Type(Unsigned32):
    """Custom type tnPtpExtTodIfPulseFormat based on Unsigned32"""
    defaultValue = 0


_TnPtpExtTodIfPulseFormat_Type.__name__ = "Unsigned32"
_TnPtpExtTodIfPulseFormat_Object = MibTableColumn
tnPtpExtTodIfPulseFormat = _TnPtpExtTodIfPulseFormat_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 4, 1, 1, 4),
    _TnPtpExtTodIfPulseFormat_Type()
)
tnPtpExtTodIfPulseFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpExtTodIfPulseFormat.setStatus("current")


class _TnPtpExtTodIfToDFormat_Type(Unsigned32):
    """Custom type tnPtpExtTodIfToDFormat based on Unsigned32"""
    defaultValue = 0


_TnPtpExtTodIfToDFormat_Type.__name__ = "Unsigned32"
_TnPtpExtTodIfToDFormat_Object = MibTableColumn
tnPtpExtTodIfToDFormat = _TnPtpExtTodIfToDFormat_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 4, 1, 1, 5),
    _TnPtpExtTodIfToDFormat_Type()
)
tnPtpExtTodIfToDFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpExtTodIfToDFormat.setStatus("current")


class _TnPtpExtTodIfCableCorrection_Type(Integer32):
    """Custom type tnPtpExtTodIfCableCorrection based on Integer32"""
    defaultValue = 0


_TnPtpExtTodIfCableCorrection_Type.__name__ = "Integer32"
_TnPtpExtTodIfCableCorrection_Object = MibTableColumn
tnPtpExtTodIfCableCorrection = _TnPtpExtTodIfCableCorrection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 4, 1, 1, 6),
    _TnPtpExtTodIfCableCorrection_Type()
)
tnPtpExtTodIfCableCorrection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpExtTodIfCableCorrection.setStatus("current")


class _TnPtpExtTodIfAdminStatus_Type(Integer32):
    """Custom type tnPtpExtTodIfAdminStatus based on Integer32"""
    defaultValue = 0


_TnPtpExtTodIfAdminStatus_Type.__name__ = "Integer32"
_TnPtpExtTodIfAdminStatus_Object = MibTableColumn
tnPtpExtTodIfAdminStatus = _TnPtpExtTodIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 4, 1, 1, 7),
    _TnPtpExtTodIfAdminStatus_Type()
)
tnPtpExtTodIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpExtTodIfAdminStatus.setStatus("current")
_TnPtpExtTodIf1ppsStatus_Type = Unsigned32
_TnPtpExtTodIf1ppsStatus_Object = MibTableColumn
tnPtpExtTodIf1ppsStatus = _TnPtpExtTodIf1ppsStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 4, 1, 1, 8),
    _TnPtpExtTodIf1ppsStatus_Type()
)
tnPtpExtTodIf1ppsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpExtTodIf1ppsStatus.setStatus("current")
_TnPtpExtTodIfToDStatus_Type = Unsigned32
_TnPtpExtTodIfToDStatus_Object = MibTableColumn
tnPtpExtTodIfToDStatus = _TnPtpExtTodIfToDStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 4, 1, 1, 9),
    _TnPtpExtTodIfToDStatus_Type()
)
tnPtpExtTodIfToDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpExtTodIfToDStatus.setStatus("current")


class _TnPtpExtTodIfAdditionalInfo_Type(OctetString):
    """Custom type tnPtpExtTodIfAdditionalInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(48, 48),
    )
    fixed_length = 48


_TnPtpExtTodIfAdditionalInfo_Type.__name__ = "OctetString"
_TnPtpExtTodIfAdditionalInfo_Object = MibTableColumn
tnPtpExtTodIfAdditionalInfo = _TnPtpExtTodIfAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 4, 1, 1, 10),
    _TnPtpExtTodIfAdditionalInfo_Type()
)
tnPtpExtTodIfAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpExtTodIfAdditionalInfo.setStatus("current")


class _TnPtpExtCompensationMode_Type(Integer32):
    """Custom type tnPtpExtCompensationMode based on Integer32"""
    defaultValue = 0


_TnPtpExtCompensationMode_Type.__name__ = "Integer32"
_TnPtpExtCompensationMode_Object = MibTableColumn
tnPtpExtCompensationMode = _TnPtpExtCompensationMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 4, 1, 1, 11),
    _TnPtpExtCompensationMode_Type()
)
tnPtpExtCompensationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpExtCompensationMode.setStatus("current")


class _TnPtpExtCompenAutoTestTrigger_Type(TruthValue):
    """Custom type tnPtpExtCompenAutoTestTrigger based on TruthValue"""
    defaultValue = 2


_TnPtpExtCompenAutoTestTrigger_Type.__name__ = "TruthValue"
_TnPtpExtCompenAutoTestTrigger_Object = MibTableColumn
tnPtpExtCompenAutoTestTrigger = _TnPtpExtCompenAutoTestTrigger_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 4, 1, 1, 12),
    _TnPtpExtCompenAutoTestTrigger_Type()
)
tnPtpExtCompenAutoTestTrigger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpExtCompenAutoTestTrigger.setStatus("current")


class _TnPtpExtCompenManualValueIn_Type(Integer32):
    """Custom type tnPtpExtCompenManualValueIn based on Integer32"""
    defaultValue = 0


_TnPtpExtCompenManualValueIn_Type.__name__ = "Integer32"
_TnPtpExtCompenManualValueIn_Object = MibTableColumn
tnPtpExtCompenManualValueIn = _TnPtpExtCompenManualValueIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 4, 1, 1, 13),
    _TnPtpExtCompenManualValueIn_Type()
)
tnPtpExtCompenManualValueIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpExtCompenManualValueIn.setStatus("current")


class _TnPtpExtCompenManualValueOut_Type(Integer32):
    """Custom type tnPtpExtCompenManualValueOut based on Integer32"""
    defaultValue = 0


_TnPtpExtCompenManualValueOut_Type.__name__ = "Integer32"
_TnPtpExtCompenManualValueOut_Object = MibTableColumn
tnPtpExtCompenManualValueOut = _TnPtpExtCompenManualValueOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 4, 1, 1, 14),
    _TnPtpExtCompenManualValueOut_Type()
)
tnPtpExtCompenManualValueOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPtpExtCompenManualValueOut.setStatus("current")


class _TnPtpExtCompenMeasureStatus_Type(Integer32):
    """Custom type tnPtpExtCompenMeasureStatus based on Integer32"""
    defaultValue = 0


_TnPtpExtCompenMeasureStatus_Type.__name__ = "Integer32"
_TnPtpExtCompenMeasureStatus_Object = MibTableColumn
tnPtpExtCompenMeasureStatus = _TnPtpExtCompenMeasureStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 1, 4, 1, 1, 15),
    _TnPtpExtCompenMeasureStatus_Type()
)
tnPtpExtCompenMeasureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpExtCompenMeasureStatus.setStatus("current")
_TnPtpConformance_ObjectIdentity = ObjectIdentity
tnPtpConformance = _TnPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 2)
)
_TnPtpGroups_ObjectIdentity = ObjectIdentity
tnPtpGroups = _TnPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 2, 1)
)
_TnPtpCompliances_ObjectIdentity = ObjectIdentity
tnPtpCompliances = _TnPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 2, 2)
)

# Managed Objects groups

tnPtpSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 2, 1, 1)
)
tnPtpSystemGroup.setObjects(
      *(("TROPIC-PTP-MIB", "tnPtpSystemClockMode"),
        ("TROPIC-PTP-MIB", "tnPtpSystemFrequencyReference"),
        ("TROPIC-PTP-MIB", "tnPtpSystemTimeReference"),
        ("TROPIC-PTP-MIB", "tnPtpSystemNextClockNumber"),
        ("TROPIC-PTP-MIB", "tnPtpSystemClockProfile"),
        ("TROPIC-PTP-MIB", "tnPtpSystemClockServoMode"))
)
if mibBuilder.loadTexts:
    tnPtpSystemGroup.setStatus("current")

tnPtpClockDefaultDSConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 2, 1, 2)
)
tnPtpClockDefaultDSConfigGroup.setObjects(
      *(("TROPIC-PTP-MIB", "tnPtpClockDefaultDSConfigDomain"),
        ("TROPIC-PTP-MIB", "tnPtpClockDefaultDSConfigPriority1"),
        ("TROPIC-PTP-MIB", "tnPtpClockDefaultDSConfigPriority2"),
        ("TROPIC-PTP-MIB", "tnPtpClockDefaultDSConfigPreferedGM"),
        ("TROPIC-PTP-MIB", "tnPtpClockDefaultDSConfigIpAddressType"),
        ("TROPIC-PTP-MIB", "tnPtpClockDefaultDSConfigIpAddress"),
        ("TROPIC-PTP-MIB", "tnPtpClockDefaultDSConfigAdminStatus"),
        ("TROPIC-PTP-MIB", "tnPtpClockDefaultDSConfigRowStatus"),
        ("TROPIC-PTP-MIB", "tnPtpClockDefaultDSConfigLocalPriority"))
)
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSConfigGroup.setStatus("current")

tnPtpClockDefaultDSInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 2, 1, 3)
)
tnPtpClockDefaultDSInfoGroup.setObjects(
      *(("TROPIC-PTP-MIB", "tnPtpClockDefaultDSInfoIdentifier"),
        ("TROPIC-PTP-MIB", "tnPtpClockDefaultDSInfoTwoStepFlag"),
        ("TROPIC-PTP-MIB", "tnPtpClockDefaultDSInfoNumberOfPorts"),
        ("TROPIC-PTP-MIB", "tnPtpClockDefaultDSInfoClass"),
        ("TROPIC-PTP-MIB", "tnPtpClockDefaultDSInfoAccuracy"),
        ("TROPIC-PTP-MIB", "tnPtpClockDefaultDSInfoOffsetScaledLogVariance"))
)
if mibBuilder.loadTexts:
    tnPtpClockDefaultDSInfoGroup.setStatus("current")

tnPtpClockCurrentDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 2, 1, 4)
)
tnPtpClockCurrentDSGroup.setObjects(
      *(("TROPIC-PTP-MIB", "tnPtpClockCurrentDSOffSetFromMaster"),
        ("TROPIC-PTP-MIB", "tnPtpClockCurrentDSMeanPathDelay"),
        ("TROPIC-PTP-MIB", "tnPtpClockCurrentDSCurrentTime"),
        ("TROPIC-PTP-MIB", "tnPtpClockCurrentDSRecoveredClockState"),
        ("TROPIC-PTP-MIB", "tnPtpClockCurrentDSLockedPtpPort"),
        ("TROPIC-PTP-MIB", "tnPtpClockCurrentDSStepsRemoved"))
)
if mibBuilder.loadTexts:
    tnPtpClockCurrentDSGroup.setStatus("current")

tnPtpClockParentDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 2, 1, 5)
)
tnPtpClockParentDSGroup.setObjects(
      *(("TROPIC-PTP-MIB", "tnPtpClockParentDSIdentifier"),
        ("TROPIC-PTP-MIB", "tnPtpClockParentDSPortNum"),
        ("TROPIC-PTP-MIB", "tnPtpClockParentDSStats"),
        ("TROPIC-PTP-MIB", "tnPtpClockParentDSOffsetScaledLogVariance"),
        ("TROPIC-PTP-MIB", "tnPtpClockParentDSPhaseChangeRate"),
        ("TROPIC-PTP-MIB", "tnPtpClockParentDSGrandmasterClockId"),
        ("TROPIC-PTP-MIB", "tnPtpClockParentDSGrandmasterClass"),
        ("TROPIC-PTP-MIB", "tnPtpClockParentDSGrandmasterAccuracy"),
        ("TROPIC-PTP-MIB", "tnPtpClockParentDSGrandmasterOffsetScaledLogVariance"),
        ("TROPIC-PTP-MIB", "tnPtpClockParentDSGrandmasterPriority1"),
        ("TROPIC-PTP-MIB", "tnPtpClockParentDSGrandmasterPriority2"))
)
if mibBuilder.loadTexts:
    tnPtpClockParentDSGroup.setStatus("current")

tnPtpClockTimePropertiesDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 2, 1, 6)
)
tnPtpClockTimePropertiesDSGroup.setObjects(
      *(("TROPIC-PTP-MIB", "tnPtpClockTimePropertiesDSCurrentUtcOffset"),
        ("TROPIC-PTP-MIB", "tnPtpClockTimePropertiesDSCurrentUtcOffsetValid"),
        ("TROPIC-PTP-MIB", "tnPtpClockTimePropertiesDSLeap59"),
        ("TROPIC-PTP-MIB", "tnPtpClockTimePropertiesDSLeap61"),
        ("TROPIC-PTP-MIB", "tnPtpClockTimePropertiesDSTimeTraceable"),
        ("TROPIC-PTP-MIB", "tnPtpClockTimePropertiesDSFrequencyTraceable"),
        ("TROPIC-PTP-MIB", "tnPtpClockTimePropertiesDSPtpTimescale"),
        ("TROPIC-PTP-MIB", "tnPtpClockTimePropertiesDSPtpTimeSource"))
)
if mibBuilder.loadTexts:
    tnPtpClockTimePropertiesDSGroup.setStatus("current")

tnPtpPortNextIndexGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 2, 1, 7)
)
tnPtpPortNextIndexGroup.setObjects(
    ("TROPIC-PTP-MIB", "tnPtpPortNextIndex")
)
if mibBuilder.loadTexts:
    tnPtpPortNextIndexGroup.setStatus("current")

tnPtpPortDSConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 2, 1, 8)
)
tnPtpPortDSConfigGroup.setObjects(
      *(("TROPIC-PTP-MIB", "tnPtpPortDSConfigAssociatedPhysicalPort"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigVlanVID"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigVlanTPID"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigAnnoRxTimeout"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigLogAnnoInterval"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigLogSyncInterval"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigLogDelayReqInterval"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigLogMinPDelayReqInterval"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigAdminStatus"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigRole"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigDelayMechanism"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigVersionNumber"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigAsymCorrection"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigTwoStepFlag"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigEncapType"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigAddressingMode"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigUnicastForDelayReq"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigUnicastNegotiation"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigDestMac"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigDestIpAddrType"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigDestIpAddr"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigRowStatus"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigConnectedPtpioTimingPort"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigAutoLinkAsyMeasureTrigger"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigNotSlave"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigLocalPriority"))
)
if mibBuilder.loadTexts:
    tnPtpPortDSConfigGroup.setStatus("current")

tnPtpPortDSInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 2, 1, 9)
)
tnPtpPortDSInfoGroup.setObjects(
      *(("TROPIC-PTP-MIB", "tnPtpPortDSInfoPeerPathDelay"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSInfoPortOperState"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSInfoNumOfSessions"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSInfoAutoLinkAsyMeasureStatus"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSInfoMeasuredLinkAsymmetry"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSInfoAnnounceMsgTx"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSInfoAnnounceMsgRx"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSInfoSyncMsgTx"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSInfoSyncMsgRx"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSInfoDelayReqMsgTx"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSInfoDelayReqMsgRx"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSInfoDelayRspMsgTx"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSInfoDelayRspMsgRx"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSInfoSignalingMsgTx"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSInfoSignalingMsgRx"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSInfoManagementMsgTx"))
)
if mibBuilder.loadTexts:
    tnPtpPortDSInfoGroup.setStatus("current")

tnPtpExtTodIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 2, 1, 11)
)
tnPtpExtTodIfGroup.setObjects(
      *(("TROPIC-PTP-MIB", "tnPtpExtTodIfDirection"),
        ("TROPIC-PTP-MIB", "tnPtpExtTodSignalValid"),
        ("TROPIC-PTP-MIB", "tnPtpExtTodIfPulseFormat"),
        ("TROPIC-PTP-MIB", "tnPtpExtTodIfToDFormat"),
        ("TROPIC-PTP-MIB", "tnPtpExtTodIfCableCorrection"),
        ("TROPIC-PTP-MIB", "tnPtpExtTodIfAdminStatus"),
        ("TROPIC-PTP-MIB", "tnPtpExtTodIf1ppsStatus"),
        ("TROPIC-PTP-MIB", "tnPtpExtTodIfToDStatus"),
        ("TROPIC-PTP-MIB", "tnPtpExtTodIfAdditionalInfo"),
        ("TROPIC-PTP-MIB", "tnPtpExtCompensationMode"),
        ("TROPIC-PTP-MIB", "tnPtpExtCompenAutoTestTrigger"),
        ("TROPIC-PTP-MIB", "tnPtpExtCompenManualValueIn"),
        ("TROPIC-PTP-MIB", "tnPtpExtCompenManualValueOut"),
        ("TROPIC-PTP-MIB", "tnPtpExtCompenMeasureStatus"))
)
if mibBuilder.loadTexts:
    tnPtpExtTodIfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 9, 2, 2, 1)
)
tnPtpCompliance.setObjects(
      *(("TROPIC-PTP-MIB", "tnPtpSystemGroup"),
        ("TROPIC-PTP-MIB", "tnPtpClockDefaultDSConfigGroup"),
        ("TROPIC-PTP-MIB", "tnPtpClockDefaultDSInfoGroup"),
        ("TROPIC-PTP-MIB", "tnPtpClockCurrentDSGroup"),
        ("TROPIC-PTP-MIB", "tnPtpClockParentDSGroup"),
        ("TROPIC-PTP-MIB", "tnPtpClockTimePropertiesDSGroup"),
        ("TROPIC-PTP-MIB", "tnPtpPortNextIndexGroup"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSConfigGroup"),
        ("TROPIC-PTP-MIB", "tnPtpPortDSInfoGroup"),
        ("TROPIC-PTP-MIB", "tnPtpExtTodIfGroup"))
)
if mibBuilder.loadTexts:
    tnPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-PTP-MIB",
    **{"InetAddressType": InetAddressType,
       "InetAddress": InetAddress,
       "AluWdmPtpClockIdentifier": AluWdmPtpClockIdentifier,
       "AluWdmPtpClockIndex": AluWdmPtpClockIndex,
       "AluWdmPtpRecoveredClockState": AluWdmPtpRecoveredClockState,
       "AluWdmtnPtpPortState": AluWdmtnPtpPortState,
       "TropicSlotIndexType": TropicSlotIndexType,
       "TropicShelfIndexType": TropicShelfIndexType,
       "tropic": tropic,
       "tropicRegistry": tropicRegistry,
       "tropicModules": tropicModules,
       "tnGenericModules": tnGenericModules,
       "tnEquipmentModules": tnEquipmentModules,
       "tnPortModules": tnPortModules,
       "tnPtpMibModule": tnPtpMibModule,
       "tropicGeneric": tropicGeneric,
       "tnEquipment": tnEquipment,
       "tnShelf": tnShelf,
       "tnShelfMIB": tnShelfMIB,
       "tnShelfObjs": tnShelfObjs,
       "tnShelfBasics": tnShelfBasics,
       "tnShelfTable": tnShelfTable,
       "tnShelfEntry": tnShelfEntry,
       "tnShelfIndex": tnShelfIndex,
       "tnSlot": tnSlot,
       "tnSlotMIB": tnSlotMIB,
       "tnSlotObjs": tnSlotObjs,
       "tnSlotBasics": tnSlotBasics,
       "tnSlotTable": tnSlotTable,
       "tnSlotEntry": tnSlotEntry,
       "tnSlotIndex": tnSlotIndex,
       "tnPort": tnPort,
       "tnPtpMIB": tnPtpMIB,
       "tnPtpMIBObjects": tnPtpMIBObjects,
       "tnPtpSystem": tnPtpSystem,
       "tnPtpSystemTable": tnPtpSystemTable,
       "tnPtpSystemEntry": tnPtpSystemEntry,
       "tnPtpSystemClockMode": tnPtpSystemClockMode,
       "tnPtpSystemFrequencyReference": tnPtpSystemFrequencyReference,
       "tnPtpSystemTimeReference": tnPtpSystemTimeReference,
       "tnPtpSystemNextClockNumber": tnPtpSystemNextClockNumber,
       "tnPtpSystemClockProfile": tnPtpSystemClockProfile,
       "tnPtpSystemClockServoMode": tnPtpSystemClockServoMode,
       "tnPtpClock": tnPtpClock,
       "tnPtpClockDefaultDSConfigTable": tnPtpClockDefaultDSConfigTable,
       "tnPtpClockDefaultDSConfigEntry": tnPtpClockDefaultDSConfigEntry,
       "tnPtpClockIndex": tnPtpClockIndex,
       "tnPtpClockDefaultDSConfigDomain": tnPtpClockDefaultDSConfigDomain,
       "tnPtpClockDefaultDSConfigPriority1": tnPtpClockDefaultDSConfigPriority1,
       "tnPtpClockDefaultDSConfigPriority2": tnPtpClockDefaultDSConfigPriority2,
       "tnPtpClockDefaultDSConfigPreferedGM": tnPtpClockDefaultDSConfigPreferedGM,
       "tnPtpClockDefaultDSConfigIpAddressType": tnPtpClockDefaultDSConfigIpAddressType,
       "tnPtpClockDefaultDSConfigIpAddress": tnPtpClockDefaultDSConfigIpAddress,
       "tnPtpClockDefaultDSConfigAdminStatus": tnPtpClockDefaultDSConfigAdminStatus,
       "tnPtpClockDefaultDSConfigRowStatus": tnPtpClockDefaultDSConfigRowStatus,
       "tnPtpClockDefaultDSConfigLocalPriority": tnPtpClockDefaultDSConfigLocalPriority,
       "tnPtpClockDefaultDSInfoTable": tnPtpClockDefaultDSInfoTable,
       "tnPtpClockDefaultDSInfoEntry": tnPtpClockDefaultDSInfoEntry,
       "tnPtpClockDefaultDSInfoIdentifier": tnPtpClockDefaultDSInfoIdentifier,
       "tnPtpClockDefaultDSInfoTwoStepFlag": tnPtpClockDefaultDSInfoTwoStepFlag,
       "tnPtpClockDefaultDSInfoNumberOfPorts": tnPtpClockDefaultDSInfoNumberOfPorts,
       "tnPtpClockDefaultDSInfoClass": tnPtpClockDefaultDSInfoClass,
       "tnPtpClockDefaultDSInfoAccuracy": tnPtpClockDefaultDSInfoAccuracy,
       "tnPtpClockDefaultDSInfoOffsetScaledLogVariance": tnPtpClockDefaultDSInfoOffsetScaledLogVariance,
       "tnPtpClockCurrentDSTable": tnPtpClockCurrentDSTable,
       "tnPtpClockCurrentDSEntry": tnPtpClockCurrentDSEntry,
       "tnPtpClockCurrentDSOffSetFromMaster": tnPtpClockCurrentDSOffSetFromMaster,
       "tnPtpClockCurrentDSMeanPathDelay": tnPtpClockCurrentDSMeanPathDelay,
       "tnPtpClockCurrentDSCurrentTime": tnPtpClockCurrentDSCurrentTime,
       "tnPtpClockCurrentDSRecoveredClockState": tnPtpClockCurrentDSRecoveredClockState,
       "tnPtpClockCurrentDSLockedPtpPort": tnPtpClockCurrentDSLockedPtpPort,
       "tnPtpClockCurrentDSStepsRemoved": tnPtpClockCurrentDSStepsRemoved,
       "tnPtpClockParentDSTable": tnPtpClockParentDSTable,
       "tnPtpClockParentDSEntry": tnPtpClockParentDSEntry,
       "tnPtpClockParentDSIdentifier": tnPtpClockParentDSIdentifier,
       "tnPtpClockParentDSPortNum": tnPtpClockParentDSPortNum,
       "tnPtpClockParentDSStats": tnPtpClockParentDSStats,
       "tnPtpClockParentDSOffsetScaledLogVariance": tnPtpClockParentDSOffsetScaledLogVariance,
       "tnPtpClockParentDSPhaseChangeRate": tnPtpClockParentDSPhaseChangeRate,
       "tnPtpClockParentDSGrandmasterClockId": tnPtpClockParentDSGrandmasterClockId,
       "tnPtpClockParentDSGrandmasterClass": tnPtpClockParentDSGrandmasterClass,
       "tnPtpClockParentDSGrandmasterAccuracy": tnPtpClockParentDSGrandmasterAccuracy,
       "tnPtpClockParentDSGrandmasterOffsetScaledLogVariance": tnPtpClockParentDSGrandmasterOffsetScaledLogVariance,
       "tnPtpClockParentDSGrandmasterPriority1": tnPtpClockParentDSGrandmasterPriority1,
       "tnPtpClockParentDSGrandmasterPriority2": tnPtpClockParentDSGrandmasterPriority2,
       "tnPtpClockTimePropertiesDSTable": tnPtpClockTimePropertiesDSTable,
       "tnPtpClockTimePropertiesDSEntry": tnPtpClockTimePropertiesDSEntry,
       "tnPtpClockTimePropertiesDSCurrentUtcOffset": tnPtpClockTimePropertiesDSCurrentUtcOffset,
       "tnPtpClockTimePropertiesDSCurrentUtcOffsetValid": tnPtpClockTimePropertiesDSCurrentUtcOffsetValid,
       "tnPtpClockTimePropertiesDSLeap59": tnPtpClockTimePropertiesDSLeap59,
       "tnPtpClockTimePropertiesDSLeap61": tnPtpClockTimePropertiesDSLeap61,
       "tnPtpClockTimePropertiesDSTimeTraceable": tnPtpClockTimePropertiesDSTimeTraceable,
       "tnPtpClockTimePropertiesDSFrequencyTraceable": tnPtpClockTimePropertiesDSFrequencyTraceable,
       "tnPtpClockTimePropertiesDSPtpTimescale": tnPtpClockTimePropertiesDSPtpTimescale,
       "tnPtpClockTimePropertiesDSPtpTimeSource": tnPtpClockTimePropertiesDSPtpTimeSource,
       "tnPtpPort": tnPtpPort,
       "tnPtpPortNextIndexTable": tnPtpPortNextIndexTable,
       "tnPtpPortNextIndexEntry": tnPtpPortNextIndexEntry,
       "tnPtpPortNextIndex": tnPtpPortNextIndex,
       "tnPtpPortDSConfigTable": tnPtpPortDSConfigTable,
       "tnPtpPortDSConfigEntry": tnPtpPortDSConfigEntry,
       "tnPtpPortDSPortIndex": tnPtpPortDSPortIndex,
       "tnPtpPortDSConfigAssociatedPhysicalPort": tnPtpPortDSConfigAssociatedPhysicalPort,
       "tnPtpPortDSConfigVlanVID": tnPtpPortDSConfigVlanVID,
       "tnPtpPortDSConfigVlanTPID": tnPtpPortDSConfigVlanTPID,
       "tnPtpPortDSConfigAnnoRxTimeout": tnPtpPortDSConfigAnnoRxTimeout,
       "tnPtpPortDSConfigLogAnnoInterval": tnPtpPortDSConfigLogAnnoInterval,
       "tnPtpPortDSConfigLogSyncInterval": tnPtpPortDSConfigLogSyncInterval,
       "tnPtpPortDSConfigLogDelayReqInterval": tnPtpPortDSConfigLogDelayReqInterval,
       "tnPtpPortDSConfigLogMinPDelayReqInterval": tnPtpPortDSConfigLogMinPDelayReqInterval,
       "tnPtpPortDSConfigAdminStatus": tnPtpPortDSConfigAdminStatus,
       "tnPtpPortDSConfigRole": tnPtpPortDSConfigRole,
       "tnPtpPortDSConfigDelayMechanism": tnPtpPortDSConfigDelayMechanism,
       "tnPtpPortDSConfigVersionNumber": tnPtpPortDSConfigVersionNumber,
       "tnPtpPortDSConfigAsymCorrection": tnPtpPortDSConfigAsymCorrection,
       "tnPtpPortDSConfigTwoStepFlag": tnPtpPortDSConfigTwoStepFlag,
       "tnPtpPortDSConfigEncapType": tnPtpPortDSConfigEncapType,
       "tnPtpPortDSConfigAddressingMode": tnPtpPortDSConfigAddressingMode,
       "tnPtpPortDSConfigUnicastForDelayReq": tnPtpPortDSConfigUnicastForDelayReq,
       "tnPtpPortDSConfigUnicastNegotiation": tnPtpPortDSConfigUnicastNegotiation,
       "tnPtpPortDSConfigDestMac": tnPtpPortDSConfigDestMac,
       "tnPtpPortDSConfigDestIpAddrType": tnPtpPortDSConfigDestIpAddrType,
       "tnPtpPortDSConfigDestIpAddr": tnPtpPortDSConfigDestIpAddr,
       "tnPtpPortDSConfigRowStatus": tnPtpPortDSConfigRowStatus,
       "tnPtpPortDSConfigConnectedPtpioTimingPort": tnPtpPortDSConfigConnectedPtpioTimingPort,
       "tnPtpPortDSConfigAutoLinkAsyMeasureTrigger": tnPtpPortDSConfigAutoLinkAsyMeasureTrigger,
       "tnPtpPortDSConfigNotSlave": tnPtpPortDSConfigNotSlave,
       "tnPtpPortDSConfigLocalPriority": tnPtpPortDSConfigLocalPriority,
       "tnPtpPortDSInfoTable": tnPtpPortDSInfoTable,
       "tnPtpPortDSInfoEntry": tnPtpPortDSInfoEntry,
       "tnPtpPortDSInfoPeerPathDelay": tnPtpPortDSInfoPeerPathDelay,
       "tnPtpPortDSInfoPortOperState": tnPtpPortDSInfoPortOperState,
       "tnPtpPortDSInfoNumOfSessions": tnPtpPortDSInfoNumOfSessions,
       "tnPtpPortDSInfoAutoLinkAsyMeasureStatus": tnPtpPortDSInfoAutoLinkAsyMeasureStatus,
       "tnPtpPortDSInfoMeasuredLinkAsymmetry": tnPtpPortDSInfoMeasuredLinkAsymmetry,
       "tnPtpPortDSInfoAnnounceMsgTx": tnPtpPortDSInfoAnnounceMsgTx,
       "tnPtpPortDSInfoAnnounceMsgRx": tnPtpPortDSInfoAnnounceMsgRx,
       "tnPtpPortDSInfoSyncMsgTx": tnPtpPortDSInfoSyncMsgTx,
       "tnPtpPortDSInfoSyncMsgRx": tnPtpPortDSInfoSyncMsgRx,
       "tnPtpPortDSInfoDelayReqMsgTx": tnPtpPortDSInfoDelayReqMsgTx,
       "tnPtpPortDSInfoDelayReqMsgRx": tnPtpPortDSInfoDelayReqMsgRx,
       "tnPtpPortDSInfoDelayRspMsgTx": tnPtpPortDSInfoDelayRspMsgTx,
       "tnPtpPortDSInfoDelayRspMsgRx": tnPtpPortDSInfoDelayRspMsgRx,
       "tnPtpPortDSInfoSignalingMsgTx": tnPtpPortDSInfoSignalingMsgTx,
       "tnPtpPortDSInfoSignalingMsgRx": tnPtpPortDSInfoSignalingMsgRx,
       "tnPtpPortDSInfoManagementMsgTx": tnPtpPortDSInfoManagementMsgTx,
       "tnPtpPortDSInfoManagementMsgRx": tnPtpPortDSInfoManagementMsgRx,
       "tnPtpPortDSInfoFollowUpMsgTx": tnPtpPortDSInfoFollowUpMsgTx,
       "tnPtpPortDSInfoFollowUpMsgRx": tnPtpPortDSInfoFollowUpMsgRx,
       "tnPtpExtTodIf": tnPtpExtTodIf,
       "tnPtpExtTodIfTable": tnPtpExtTodIfTable,
       "tnPtpExtTodIfEntry": tnPtpExtTodIfEntry,
       "tnPtpExtTodIfIndex": tnPtpExtTodIfIndex,
       "tnPtpExtTodIfDirection": tnPtpExtTodIfDirection,
       "tnPtpExtTodSignalValid": tnPtpExtTodSignalValid,
       "tnPtpExtTodIfPulseFormat": tnPtpExtTodIfPulseFormat,
       "tnPtpExtTodIfToDFormat": tnPtpExtTodIfToDFormat,
       "tnPtpExtTodIfCableCorrection": tnPtpExtTodIfCableCorrection,
       "tnPtpExtTodIfAdminStatus": tnPtpExtTodIfAdminStatus,
       "tnPtpExtTodIf1ppsStatus": tnPtpExtTodIf1ppsStatus,
       "tnPtpExtTodIfToDStatus": tnPtpExtTodIfToDStatus,
       "tnPtpExtTodIfAdditionalInfo": tnPtpExtTodIfAdditionalInfo,
       "tnPtpExtCompensationMode": tnPtpExtCompensationMode,
       "tnPtpExtCompenAutoTestTrigger": tnPtpExtCompenAutoTestTrigger,
       "tnPtpExtCompenManualValueIn": tnPtpExtCompenManualValueIn,
       "tnPtpExtCompenManualValueOut": tnPtpExtCompenManualValueOut,
       "tnPtpExtCompenMeasureStatus": tnPtpExtCompenMeasureStatus,
       "tnPtpConformance": tnPtpConformance,
       "tnPtpGroups": tnPtpGroups,
       "tnPtpSystemGroup": tnPtpSystemGroup,
       "tnPtpClockDefaultDSConfigGroup": tnPtpClockDefaultDSConfigGroup,
       "tnPtpClockDefaultDSInfoGroup": tnPtpClockDefaultDSInfoGroup,
       "tnPtpClockCurrentDSGroup": tnPtpClockCurrentDSGroup,
       "tnPtpClockParentDSGroup": tnPtpClockParentDSGroup,
       "tnPtpClockTimePropertiesDSGroup": tnPtpClockTimePropertiesDSGroup,
       "tnPtpPortNextIndexGroup": tnPtpPortNextIndexGroup,
       "tnPtpPortDSConfigGroup": tnPtpPortDSConfigGroup,
       "tnPtpPortDSInfoGroup": tnPtpPortDSInfoGroup,
       "tnPtpExtTodIfGroup": tnPtpExtTodIfGroup,
       "tnPtpCompliances": tnPtpCompliances,
       "tnPtpCompliance": tnPtpCompliance}
)
