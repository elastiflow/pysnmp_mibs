# SNMP MIB module (E7-Calix-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/calix_6321/E7-Calix-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 17:40:54 2025
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

(e7,
 e7Modules) = mibBuilder.importSymbols(
    "CALIX-PRODUCT-MIB",
    "e7",
    "e7Modules")

(E7AdminStatus,
 E7CardType,
 E7EtherType,
 E7Pbit,
 E7PowerLevel,
 E7SnmpVers) = mibBuilder.importSymbols(
    "E7-TC",
    "E7AdminStatus",
    "E7CardType",
    "E7EtherType",
    "E7Pbit",
    "E7PowerLevel",
    "E7SnmpVers")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

e7ResourceModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_E7Resource_ObjectIdentity = ObjectIdentity
e7Resource = _E7Resource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2)
)
_E7NodeResource_ObjectIdentity = ObjectIdentity
e7NodeResource = _E7NodeResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1)
)
_E7CraftGroup_ObjectIdentity = ObjectIdentity
e7CraftGroup = _E7CraftGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 4)
)
_E7CraftUserGroup_ObjectIdentity = ObjectIdentity
e7CraftUserGroup = _E7CraftUserGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 5)
)
_E7CardGroup_ObjectIdentity = ObjectIdentity
e7CardGroup = _E7CardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6)
)
_E7CardTable_Object = MibTable
e7CardTable = _E7CardTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    e7CardTable.setStatus("current")
_E7CardEntry_Object = MibTableRow
e7CardEntry = _E7CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 1, 1)
)
e7CardEntry.setIndexNames(
    (0, "E7-Calix-MIB", "e7CardBank"),
    (0, "E7-Calix-MIB", "e7CardIndex"),
)
if mibBuilder.loadTexts:
    e7CardEntry.setStatus("current")
_E7CardBank_Type = Integer32
_E7CardBank_Object = MibTableColumn
e7CardBank = _E7CardBank_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 1, 1, 1),
    _E7CardBank_Type()
)
e7CardBank.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7CardBank.setStatus("current")
_E7CardIndex_Type = Integer32
_E7CardIndex_Object = MibTableColumn
e7CardIndex = _E7CardIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 1, 1, 2),
    _E7CardIndex_Type()
)
e7CardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7CardIndex.setStatus("current")
_E7CardRowStatus_Type = RowStatus
_E7CardRowStatus_Object = MibTableColumn
e7CardRowStatus = _E7CardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 1, 1, 3),
    _E7CardRowStatus_Type()
)
e7CardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7CardRowStatus.setStatus("current")
_E7CardAdminStatus_Type = E7AdminStatus
_E7CardAdminStatus_Object = MibTableColumn
e7CardAdminStatus = _E7CardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 1, 1, 4),
    _E7CardAdminStatus_Type()
)
e7CardAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7CardAdminStatus.setStatus("current")
_E7CardProvType_Type = E7CardType
_E7CardProvType_Object = MibTableColumn
e7CardProvType = _E7CardProvType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 1, 1, 5),
    _E7CardProvType_Type()
)
e7CardProvType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7CardProvType.setStatus("current")
_E7CardActualType_Type = E7CardType
_E7CardActualType_Object = MibTableColumn
e7CardActualType = _E7CardActualType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 1, 1, 6),
    _E7CardActualType_Type()
)
e7CardActualType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7CardActualType.setStatus("current")
_E7CardSoftwareVersion_Type = OctetString
_E7CardSoftwareVersion_Object = MibTableColumn
e7CardSoftwareVersion = _E7CardSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 1, 1, 7),
    _E7CardSoftwareVersion_Type()
)
e7CardSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7CardSoftwareVersion.setStatus("current")
_E7CardSerialNumber_Type = DisplayString
_E7CardSerialNumber_Object = MibTableColumn
e7CardSerialNumber = _E7CardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 1, 1, 8),
    _E7CardSerialNumber_Type()
)
e7CardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7CardSerialNumber.setStatus("current")
_E7CardCurrentPowerLevel_Type = E7PowerLevel
_E7CardCurrentPowerLevel_Object = MibTableColumn
e7CardCurrentPowerLevel = _E7CardCurrentPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 1, 1, 9),
    _E7CardCurrentPowerLevel_Type()
)
e7CardCurrentPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7CardCurrentPowerLevel.setStatus("current")
_E7CardCleiCode_Type = OctetString
_E7CardCleiCode_Object = MibTableColumn
e7CardCleiCode = _E7CardCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 1, 1, 10),
    _E7CardCleiCode_Type()
)
e7CardCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7CardCleiCode.setStatus("current")
_E7CardPartNumber_Type = OctetString
_E7CardPartNumber_Object = MibTableColumn
e7CardPartNumber = _E7CardPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 1, 1, 11),
    _E7CardPartNumber_Type()
)
e7CardPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7CardPartNumber.setStatus("current")
_E7CardStartMacRange_Type = OctetString
_E7CardStartMacRange_Object = MibTableColumn
e7CardStartMacRange = _E7CardStartMacRange_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 1, 1, 12),
    _E7CardStartMacRange_Type()
)
e7CardStartMacRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7CardStartMacRange.setStatus("current")
_E7CardEndMacRange_Type = OctetString
_E7CardEndMacRange_Object = MibTableColumn
e7CardEndMacRange = _E7CardEndMacRange_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 1, 1, 13),
    _E7CardEndMacRange_Type()
)
e7CardEndMacRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7CardEndMacRange.setStatus("current")
_E7OltPonPortTable_Object = MibTable
e7OltPonPortTable = _E7OltPonPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    e7OltPonPortTable.setStatus("current")
_E7OltPonPortEntry_Object = MibTableRow
e7OltPonPortEntry = _E7OltPonPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 2, 1)
)
e7OltPonPortEntry.setIndexNames(
    (0, "E7-Calix-MIB", "e7OltPonPortShelf"),
    (0, "E7-Calix-MIB", "e7OltPonPortSlot"),
    (0, "E7-Calix-MIB", "e7OltPonPortId"),
)
if mibBuilder.loadTexts:
    e7OltPonPortEntry.setStatus("current")
_E7OltPonPortShelf_Type = Integer32
_E7OltPonPortShelf_Object = MibTableColumn
e7OltPonPortShelf = _E7OltPonPortShelf_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 2, 1, 1),
    _E7OltPonPortShelf_Type()
)
e7OltPonPortShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7OltPonPortShelf.setStatus("current")
_E7OltPonPortSlot_Type = Integer32
_E7OltPonPortSlot_Object = MibTableColumn
e7OltPonPortSlot = _E7OltPonPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 2, 1, 2),
    _E7OltPonPortSlot_Type()
)
e7OltPonPortSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7OltPonPortSlot.setStatus("current")
_E7OltPonPortId_Type = Integer32
_E7OltPonPortId_Object = MibTableColumn
e7OltPonPortId = _E7OltPonPortId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 2, 1, 3),
    _E7OltPonPortId_Type()
)
e7OltPonPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7OltPonPortId.setStatus("current")


class _E7OltPonPortStatus_Type(Integer32):
    """Custom type e7OltPonPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("linkUp", 1),
          ("linkDown", 2))
    )


_E7OltPonPortStatus_Type.__name__ = "Integer32"
_E7OltPonPortStatus_Object = MibTableColumn
e7OltPonPortStatus = _E7OltPonPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 2, 1, 4),
    _E7OltPonPortStatus_Type()
)
e7OltPonPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7OltPonPortStatus.setStatus("current")
_E7OltPonPortTemperature_Type = Integer32
_E7OltPonPortTemperature_Object = MibTableColumn
e7OltPonPortTemperature = _E7OltPonPortTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 2, 1, 5),
    _E7OltPonPortTemperature_Type()
)
e7OltPonPortTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7OltPonPortTemperature.setStatus("current")
_E7OltPonPortTxBias_Type = Integer32
_E7OltPonPortTxBias_Object = MibTableColumn
e7OltPonPortTxBias = _E7OltPonPortTxBias_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 2, 1, 6),
    _E7OltPonPortTxBias_Type()
)
e7OltPonPortTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7OltPonPortTxBias.setStatus("current")
_E7OltPonPortTxPower_Type = Integer32
_E7OltPonPortTxPower_Object = MibTableColumn
e7OltPonPortTxPower = _E7OltPonPortTxPower_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 2, 1, 7),
    _E7OltPonPortTxPower_Type()
)
e7OltPonPortTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7OltPonPortTxPower.setStatus("current")
_E7OltPonPortRxPower_Type = Integer32
_E7OltPonPortRxPower_Object = MibTableColumn
e7OltPonPortRxPower = _E7OltPonPortRxPower_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 2, 1, 8),
    _E7OltPonPortRxPower_Type()
)
e7OltPonPortRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7OltPonPortRxPower.setStatus("current")
_E7OltPonPortVoltage_Type = Integer32
_E7OltPonPortVoltage_Object = MibTableColumn
e7OltPonPortVoltage = _E7OltPonPortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 6, 2, 1, 9),
    _E7OltPonPortVoltage_Type()
)
e7OltPonPortVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7OltPonPortVoltage.setStatus("current")
_E7SystemGroup_ObjectIdentity = ObjectIdentity
e7SystemGroup = _E7SystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 7)
)
_E7SystemId_Type = OctetString
_E7SystemId_Object = MibScalar
e7SystemId = _E7SystemId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 7, 1),
    _E7SystemId_Type()
)
e7SystemId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7SystemId.setStatus("current")
_E7SystemLocation_Type = OctetString
_E7SystemLocation_Object = MibScalar
e7SystemLocation = _E7SystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 7, 2),
    _E7SystemLocation_Type()
)
e7SystemLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7SystemLocation.setStatus("current")


class _E7SystemAutoUpgrade_Type(Integer32):
    """Custom type e7SystemAutoUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_E7SystemAutoUpgrade_Type.__name__ = "Integer32"
_E7SystemAutoUpgrade_Object = MibScalar
e7SystemAutoUpgrade = _E7SystemAutoUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 7, 3),
    _E7SystemAutoUpgrade_Type()
)
e7SystemAutoUpgrade.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7SystemAutoUpgrade.setStatus("current")


class _E7SystemTelnetServer_Type(Integer32):
    """Custom type e7SystemTelnetServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_E7SystemTelnetServer_Type.__name__ = "Integer32"
_E7SystemTelnetServer_Object = MibScalar
e7SystemTelnetServer = _E7SystemTelnetServer_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 7, 4),
    _E7SystemTelnetServer_Type()
)
e7SystemTelnetServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7SystemTelnetServer.setStatus("current")


class _E7SystemUnsecuredWeb_Type(Integer32):
    """Custom type e7SystemUnsecuredWeb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_E7SystemUnsecuredWeb_Type.__name__ = "Integer32"
_E7SystemUnsecuredWeb_Object = MibScalar
e7SystemUnsecuredWeb = _E7SystemUnsecuredWeb_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 7, 5),
    _E7SystemUnsecuredWeb_Type()
)
e7SystemUnsecuredWeb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7SystemUnsecuredWeb.setStatus("current")
_E7SystemPasswordExpiry_Type = Integer32
_E7SystemPasswordExpiry_Object = MibScalar
e7SystemPasswordExpiry = _E7SystemPasswordExpiry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 7, 6),
    _E7SystemPasswordExpiry_Type()
)
e7SystemPasswordExpiry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7SystemPasswordExpiry.setStatus("current")
_E7SystemDnsPrimary_Type = IpAddress
_E7SystemDnsPrimary_Object = MibScalar
e7SystemDnsPrimary = _E7SystemDnsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 7, 7),
    _E7SystemDnsPrimary_Type()
)
e7SystemDnsPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7SystemDnsPrimary.setStatus("current")
_E7SystemDnsSecondary_Type = IpAddress
_E7SystemDnsSecondary_Object = MibScalar
e7SystemDnsSecondary = _E7SystemDnsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 7, 8),
    _E7SystemDnsSecondary_Type()
)
e7SystemDnsSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7SystemDnsSecondary.setStatus("current")
_E7SystemTimezone_Type = OctetString
_E7SystemTimezone_Object = MibScalar
e7SystemTimezone = _E7SystemTimezone_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 7, 9),
    _E7SystemTimezone_Type()
)
e7SystemTimezone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7SystemTimezone.setStatus("current")
_E7SystemChassisSerialNumber_Type = OctetString
_E7SystemChassisSerialNumber_Object = MibScalar
e7SystemChassisSerialNumber = _E7SystemChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 7, 10),
    _E7SystemChassisSerialNumber_Type()
)
e7SystemChassisSerialNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7SystemChassisSerialNumber.setStatus("current")
_E7SystemChassisMacAddress_Type = MacAddress
_E7SystemChassisMacAddress_Object = MibScalar
e7SystemChassisMacAddress = _E7SystemChassisMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 7, 11),
    _E7SystemChassisMacAddress_Type()
)
e7SystemChassisMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7SystemChassisMacAddress.setStatus("current")
_E7SystemTime_Type = DisplayString
_E7SystemTime_Object = MibScalar
e7SystemTime = _E7SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 7, 12),
    _E7SystemTime_Type()
)
e7SystemTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7SystemTime.setStatus("current")
_E7SystemDate_Type = DisplayString
_E7SystemDate_Object = MibScalar
e7SystemDate = _E7SystemDate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 7, 13),
    _E7SystemDate_Type()
)
e7SystemDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7SystemDate.setStatus("current")
_E7PortGroup_ObjectIdentity = ObjectIdentity
e7PortGroup = _E7PortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9)
)
_E7VdslPortGroup_ObjectIdentity = ObjectIdentity
e7VdslPortGroup = _E7VdslPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1)
)
_E7VdslPortTable_Object = MibTable
e7VdslPortTable = _E7VdslPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    e7VdslPortTable.setStatus("current")
_E7VdslPortEntry_Object = MibTableRow
e7VdslPortEntry = _E7VdslPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 1, 1)
)
e7VdslPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    e7VdslPortEntry.setStatus("current")
_E7VdslPortRowStatus_Type = RowStatus
_E7VdslPortRowStatus_Object = MibTableColumn
e7VdslPortRowStatus = _E7VdslPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 1, 1, 1),
    _E7VdslPortRowStatus_Type()
)
e7VdslPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7VdslPortRowStatus.setStatus("current")
_E7VdslPortAdminStatus_Type = E7AdminStatus
_E7VdslPortAdminStatus_Object = MibTableColumn
e7VdslPortAdminStatus = _E7VdslPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 1, 1, 2),
    _E7VdslPortAdminStatus_Type()
)
e7VdslPortAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7VdslPortAdminStatus.setStatus("current")
_E7VdslPortCurrTxRate_Type = Integer32
_E7VdslPortCurrTxRate_Object = MibTableColumn
e7VdslPortCurrTxRate = _E7VdslPortCurrTxRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 1, 1, 3),
    _E7VdslPortCurrTxRate_Type()
)
e7VdslPortCurrTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7VdslPortCurrTxRate.setStatus("current")
_E7VdslPortCurrRxRate_Type = Integer32
_E7VdslPortCurrRxRate_Object = MibTableColumn
e7VdslPortCurrRxRate = _E7VdslPortCurrRxRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 1, 1, 4),
    _E7VdslPortCurrRxRate_Type()
)
e7VdslPortCurrRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7VdslPortCurrRxRate.setStatus("current")


class _E7VdslPortStatsProtocol_Type(Integer32):
    """Custom type e7VdslPortStatsProtocol based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vdsl8a", 2),
          ("vdsl8b", 3),
          ("vdsl8c", 4),
          ("vdsl8d", 5),
          ("vdsl12a", 6),
          ("vdsl12b", 7),
          ("vdsl17a", 8),
          ("gdmt", 9),
          ("glite", 10),
          ("adsl2", 11),
          ("adsl2plus", 12),
          ("t1413", 13))
    )


_E7VdslPortStatsProtocol_Type.__name__ = "Integer32"
_E7VdslPortStatsProtocol_Object = MibTableColumn
e7VdslPortStatsProtocol = _E7VdslPortStatsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 1, 1, 5),
    _E7VdslPortStatsProtocol_Type()
)
e7VdslPortStatsProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7VdslPortStatsProtocol.setStatus("current")


class _E7VdslPortLineState_Type(Integer32):
    """Custom type e7VdslPortLineState based on Integer32"""
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
        *(("idleNotConfigured", 1),
          ("idleConfigured", 2),
          ("initialization", 3),
          ("training", 4),
          ("showtime", 5),
          ("showtimeL2", 6),
          ("ldInit", 7),
          ("ldFetch", 8),
          ("ldDone", 9),
          ("ldFailed", 10))
    )


_E7VdslPortLineState_Type.__name__ = "Integer32"
_E7VdslPortLineState_Object = MibTableColumn
e7VdslPortLineState = _E7VdslPortLineState_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 1, 1, 6),
    _E7VdslPortLineState_Type()
)
e7VdslPortLineState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7VdslPortLineState.setStatus("current")
_E7VdslRateTable_Object = MibTable
e7VdslRateTable = _E7VdslRateTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    e7VdslRateTable.setStatus("current")
_E7VdslRateEntry_Object = MibTableRow
e7VdslRateEntry = _E7VdslRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 2, 1)
)
e7VdslRateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    e7VdslRateEntry.setStatus("current")
_E7VdslRateRowStatus_Type = RowStatus
_E7VdslRateRowStatus_Object = MibTableColumn
e7VdslRateRowStatus = _E7VdslRateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 2, 1, 1),
    _E7VdslRateRowStatus_Type()
)
e7VdslRateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7VdslRateRowStatus.setStatus("current")
_E7VdslRateAdminStatus_Type = E7AdminStatus
_E7VdslRateAdminStatus_Object = MibTableColumn
e7VdslRateAdminStatus = _E7VdslRateAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 2, 1, 2),
    _E7VdslRateAdminStatus_Type()
)
e7VdslRateAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7VdslRateAdminStatus.setStatus("current")
_E7VdslRateProvDataRateUs_Type = Integer32
_E7VdslRateProvDataRateUs_Object = MibTableColumn
e7VdslRateProvDataRateUs = _E7VdslRateProvDataRateUs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 2, 1, 3),
    _E7VdslRateProvDataRateUs_Type()
)
e7VdslRateProvDataRateUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7VdslRateProvDataRateUs.setStatus("current")
_E7VdslRateProvDataRateDs_Type = Integer32
_E7VdslRateProvDataRateDs_Object = MibTableColumn
e7VdslRateProvDataRateDs = _E7VdslRateProvDataRateDs_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 2, 1, 4),
    _E7VdslRateProvDataRateDs_Type()
)
e7VdslRateProvDataRateDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7VdslRateProvDataRateDs.setStatus("current")
_E7VdslPhysTable_Object = MibTable
e7VdslPhysTable = _E7VdslPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 3)
)
if mibBuilder.loadTexts:
    e7VdslPhysTable.setStatus("current")
_E7VdslPhysEntry_Object = MibTableRow
e7VdslPhysEntry = _E7VdslPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 3, 1)
)
e7VdslPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E7-Calix-MIB", "e7VdslPhysSide"),
)
if mibBuilder.loadTexts:
    e7VdslPhysEntry.setStatus("current")


class _E7VdslPhysSide_Type(Integer32):
    """Custom type e7VdslPhysSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 1),
          ("upstream", 2))
    )


_E7VdslPhysSide_Type.__name__ = "Integer32"
_E7VdslPhysSide_Object = MibTableColumn
e7VdslPhysSide = _E7VdslPhysSide_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 3, 1, 1),
    _E7VdslPhysSide_Type()
)
e7VdslPhysSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7VdslPhysSide.setStatus("current")


class _E7VdslPhysCurrSnrMargin_Type(Integer32):
    """Custom type e7VdslPhysCurrSnrMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-640, 630),
    )


_E7VdslPhysCurrSnrMargin_Type.__name__ = "Integer32"
_E7VdslPhysCurrSnrMargin_Object = MibTableColumn
e7VdslPhysCurrSnrMargin = _E7VdslPhysCurrSnrMargin_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 3, 1, 2),
    _E7VdslPhysCurrSnrMargin_Type()
)
e7VdslPhysCurrSnrMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7VdslPhysCurrSnrMargin.setStatus("current")
if mibBuilder.loadTexts:
    e7VdslPhysCurrSnrMargin.setUnits("0.1dBm")


class _E7VdslPhysCurrAtn_Type(Integer32):
    """Custom type e7VdslPhysCurrAtn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1280),
    )


_E7VdslPhysCurrAtn_Type.__name__ = "Integer32"
_E7VdslPhysCurrAtn_Object = MibTableColumn
e7VdslPhysCurrAtn = _E7VdslPhysCurrAtn_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 3, 1, 3),
    _E7VdslPhysCurrAtn_Type()
)
e7VdslPhysCurrAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7VdslPhysCurrAtn.setStatus("current")
if mibBuilder.loadTexts:
    e7VdslPhysCurrAtn.setUnits("0.1dBm")


class _E7VdslPhysCurrOutputPwr_Type(Integer32):
    """Custom type e7VdslPhysCurrOutputPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-310, 310),
    )


_E7VdslPhysCurrOutputPwr_Type.__name__ = "Integer32"
_E7VdslPhysCurrOutputPwr_Object = MibTableColumn
e7VdslPhysCurrOutputPwr = _E7VdslPhysCurrOutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 3, 1, 4),
    _E7VdslPhysCurrOutputPwr_Type()
)
e7VdslPhysCurrOutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7VdslPhysCurrOutputPwr.setStatus("current")
if mibBuilder.loadTexts:
    e7VdslPhysCurrOutputPwr.setUnits("0.1dBm")
_E7VdslPhysInterleaveDelay_Type = Integer32
_E7VdslPhysInterleaveDelay_Object = MibTableColumn
e7VdslPhysInterleaveDelay = _E7VdslPhysInterleaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 3, 1, 5),
    _E7VdslPhysInterleaveDelay_Type()
)
e7VdslPhysInterleaveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7VdslPhysInterleaveDelay.setStatus("current")
_E7VdslPhysImpulseNoiseProtection_Type = Integer32
_E7VdslPhysImpulseNoiseProtection_Object = MibTableColumn
e7VdslPhysImpulseNoiseProtection = _E7VdslPhysImpulseNoiseProtection_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 3, 1, 6),
    _E7VdslPhysImpulseNoiseProtection_Type()
)
e7VdslPhysImpulseNoiseProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7VdslPhysImpulseNoiseProtection.setStatus("current")
if mibBuilder.loadTexts:
    e7VdslPhysImpulseNoiseProtection.setUnits("0.1 symbol")


class _E7VdslPhysTransmissionMode_Type(Integer32):
    """Custom type e7VdslPhysTransmissionMode based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("t1413", 1),
          ("vdsl2a", 2),
          ("gdmt", 3),
          ("adsl2m", 4),
          ("adsl2plusm", 5),
          ("glite", 6),
          ("vdsl2b", 7),
          ("vdsl2c", 8),
          ("vdsl2", 9),
          ("readsl12", 10),
          ("adsl2plus", 11),
          ("adsl2", 12))
    )


_E7VdslPhysTransmissionMode_Type.__name__ = "Integer32"
_E7VdslPhysTransmissionMode_Object = MibTableColumn
e7VdslPhysTransmissionMode = _E7VdslPhysTransmissionMode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 3, 1, 7),
    _E7VdslPhysTransmissionMode_Type()
)
e7VdslPhysTransmissionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7VdslPhysTransmissionMode.setStatus("current")
_E7VdslPortCfgTable_Object = MibTable
e7VdslPortCfgTable = _E7VdslPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4)
)
if mibBuilder.loadTexts:
    e7VdslPortCfgTable.setStatus("current")
_E7VdslPortCfgEntry_Object = MibTableRow
e7VdslPortCfgEntry = _E7VdslPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1)
)
e7VdslPortCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    e7VdslPortCfgEntry.setStatus("current")


class _E7VdslPortCfgServiceType_Type(Integer32):
    """Custom type e7VdslPortCfgServiceType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("auto", 1),
          ("mm", 2),
          ("mm2plus", 3),
          ("t1413", 4),
          ("gdmt", 5),
          ("glite", 6),
          ("adsl2", 7),
          ("adsl2plus", 8),
          ("readsl2", 9),
          ("annexm", 10),
          ("vdsl2", 11),
          ("vdsl2mm", 12))
    )


_E7VdslPortCfgServiceType_Type.__name__ = "Integer32"
_E7VdslPortCfgServiceType_Object = MibTableColumn
e7VdslPortCfgServiceType = _E7VdslPortCfgServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1, 1),
    _E7VdslPortCfgServiceType_Type()
)
e7VdslPortCfgServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgServiceType.setStatus("current")


class _E7VdslPortCfgPathLatency_Type(Integer32):
    """Custom type e7VdslPortCfgPathLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("fast", 1),
          ("interleaved", 2))
    )


_E7VdslPortCfgPathLatency_Type.__name__ = "Integer32"
_E7VdslPortCfgPathLatency_Object = MibTableColumn
e7VdslPortCfgPathLatency = _E7VdslPortCfgPathLatency_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1, 2),
    _E7VdslPortCfgPathLatency_Type()
)
e7VdslPortCfgPathLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgPathLatency.setStatus("current")


class _E7VdslPortCfgVdslProfile_Type(Integer32):
    """Custom type e7VdslPortCfgVdslProfile based on Integer32"""
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
        *(("none", 0),
          ("auto", 1),
          ("vdsl8a", 2),
          ("vdsl8b", 3),
          ("vdsl8c", 4),
          ("vdsl8d", 5),
          ("vdsl12a", 6),
          ("vdsl12b", 7),
          ("vdsl17a", 8),
          ("vdsl30a", 9))
    )


_E7VdslPortCfgVdslProfile_Type.__name__ = "Integer32"
_E7VdslPortCfgVdslProfile_Object = MibTableColumn
e7VdslPortCfgVdslProfile = _E7VdslPortCfgVdslProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1, 3),
    _E7VdslPortCfgVdslProfile_Type()
)
e7VdslPortCfgVdslProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgVdslProfile.setStatus("current")
_E7VdslPortCfgDsMinRate_Type = Integer32
_E7VdslPortCfgDsMinRate_Object = MibTableColumn
e7VdslPortCfgDsMinRate = _E7VdslPortCfgDsMinRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1, 4),
    _E7VdslPortCfgDsMinRate_Type()
)
e7VdslPortCfgDsMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgDsMinRate.setStatus("current")
_E7VdslPortCfgDsMaxRate_Type = Integer32
_E7VdslPortCfgDsMaxRate_Object = MibTableColumn
e7VdslPortCfgDsMaxRate = _E7VdslPortCfgDsMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1, 5),
    _E7VdslPortCfgDsMaxRate_Type()
)
e7VdslPortCfgDsMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgDsMaxRate.setStatus("current")
_E7VdslPortCfgUsMinRate_Type = Integer32
_E7VdslPortCfgUsMinRate_Object = MibTableColumn
e7VdslPortCfgUsMinRate = _E7VdslPortCfgUsMinRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1, 6),
    _E7VdslPortCfgUsMinRate_Type()
)
e7VdslPortCfgUsMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgUsMinRate.setStatus("current")
_E7VdslPortCfgUsMaxRate_Type = Integer32
_E7VdslPortCfgUsMaxRate_Object = MibTableColumn
e7VdslPortCfgUsMaxRate = _E7VdslPortCfgUsMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1, 7),
    _E7VdslPortCfgUsMaxRate_Type()
)
e7VdslPortCfgUsMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgUsMaxRate.setStatus("current")


class _E7VdslPortCfgDsMinInp_Type(Integer32):
    """Custom type e7VdslPortCfgDsMinInp based on Integer32"""
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
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("none", 1),
          ("halfSym", 2),
          ("oneSym", 3),
          ("twoSym", 4),
          ("threeSym", 5),
          ("fourSym", 6),
          ("fiveSym", 7),
          ("sixSym", 8),
          ("sevenSym", 9),
          ("eightSym", 10),
          ("nineSym", 11),
          ("tenSym", 12),
          ("elevenSym", 13),
          ("twelveSym", 14),
          ("thirteenSym", 15),
          ("fourteenSym", 16),
          ("fifteenSym", 17),
          ("sixteenSym", 18))
    )


_E7VdslPortCfgDsMinInp_Type.__name__ = "Integer32"
_E7VdslPortCfgDsMinInp_Object = MibTableColumn
e7VdslPortCfgDsMinInp = _E7VdslPortCfgDsMinInp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1, 8),
    _E7VdslPortCfgDsMinInp_Type()
)
e7VdslPortCfgDsMinInp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgDsMinInp.setStatus("current")


class _E7VdslPortCfgUsMinInp_Type(Integer32):
    """Custom type e7VdslPortCfgUsMinInp based on Integer32"""
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
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("none", 1),
          ("halfSym", 2),
          ("oneSym", 3),
          ("twoSym", 4),
          ("threeSym", 5),
          ("fourSym", 6),
          ("fiveSym", 7),
          ("sixSym", 8),
          ("sevenSym", 9),
          ("eightSym", 10),
          ("nineSym", 11),
          ("tenSym", 12),
          ("elevenSym", 13),
          ("twelveSym", 14),
          ("thirteenSym", 15),
          ("fourteenSym", 16),
          ("fifteenSym", 17),
          ("sixteenSym", 18))
    )


_E7VdslPortCfgUsMinInp_Type.__name__ = "Integer32"
_E7VdslPortCfgUsMinInp_Object = MibTableColumn
e7VdslPortCfgUsMinInp = _E7VdslPortCfgUsMinInp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1, 9),
    _E7VdslPortCfgUsMinInp_Type()
)
e7VdslPortCfgUsMinInp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgUsMinInp.setStatus("current")
_E7VdslPortCfgDsInterleaveMaxLatency_Type = Integer32
_E7VdslPortCfgDsInterleaveMaxLatency_Object = MibTableColumn
e7VdslPortCfgDsInterleaveMaxLatency = _E7VdslPortCfgDsInterleaveMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1, 10),
    _E7VdslPortCfgDsInterleaveMaxLatency_Type()
)
e7VdslPortCfgDsInterleaveMaxLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgDsInterleaveMaxLatency.setStatus("current")
_E7VdslPortCfgUsInterleaveMaxLatency_Type = Integer32
_E7VdslPortCfgUsInterleaveMaxLatency_Object = MibTableColumn
e7VdslPortCfgUsInterleaveMaxLatency = _E7VdslPortCfgUsInterleaveMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1, 11),
    _E7VdslPortCfgUsInterleaveMaxLatency_Type()
)
e7VdslPortCfgUsInterleaveMaxLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgUsInterleaveMaxLatency.setStatus("current")
_E7VdslPortCfgDsMinSnr_Type = Integer32
_E7VdslPortCfgDsMinSnr_Object = MibTableColumn
e7VdslPortCfgDsMinSnr = _E7VdslPortCfgDsMinSnr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1, 12),
    _E7VdslPortCfgDsMinSnr_Type()
)
e7VdslPortCfgDsMinSnr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgDsMinSnr.setStatus("current")
if mibBuilder.loadTexts:
    e7VdslPortCfgDsMinSnr.setUnits("0.1 dB")
_E7VdslPortCfgDsMaxSnr_Type = Integer32
_E7VdslPortCfgDsMaxSnr_Object = MibTableColumn
e7VdslPortCfgDsMaxSnr = _E7VdslPortCfgDsMaxSnr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1, 13),
    _E7VdslPortCfgDsMaxSnr_Type()
)
e7VdslPortCfgDsMaxSnr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgDsMaxSnr.setStatus("current")
if mibBuilder.loadTexts:
    e7VdslPortCfgDsMaxSnr.setUnits("0.1 dB")
_E7VdslPortCfgDsTargetSnr_Type = Integer32
_E7VdslPortCfgDsTargetSnr_Object = MibTableColumn
e7VdslPortCfgDsTargetSnr = _E7VdslPortCfgDsTargetSnr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1, 14),
    _E7VdslPortCfgDsTargetSnr_Type()
)
e7VdslPortCfgDsTargetSnr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgDsTargetSnr.setStatus("current")
if mibBuilder.loadTexts:
    e7VdslPortCfgDsTargetSnr.setUnits("0.1 dB")
_E7VdslPortCfgUsMinSnr_Type = Integer32
_E7VdslPortCfgUsMinSnr_Object = MibTableColumn
e7VdslPortCfgUsMinSnr = _E7VdslPortCfgUsMinSnr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1, 15),
    _E7VdslPortCfgUsMinSnr_Type()
)
e7VdslPortCfgUsMinSnr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgUsMinSnr.setStatus("current")
if mibBuilder.loadTexts:
    e7VdslPortCfgUsMinSnr.setUnits("0.1 dB")
_E7VdslPortCfgUsMaxSnr_Type = Integer32
_E7VdslPortCfgUsMaxSnr_Object = MibTableColumn
e7VdslPortCfgUsMaxSnr = _E7VdslPortCfgUsMaxSnr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1, 16),
    _E7VdslPortCfgUsMaxSnr_Type()
)
e7VdslPortCfgUsMaxSnr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgUsMaxSnr.setStatus("current")
if mibBuilder.loadTexts:
    e7VdslPortCfgUsMaxSnr.setUnits("0.1 dB")
_E7VdslPortCfgUsTargetSnr_Type = Integer32
_E7VdslPortCfgUsTargetSnr_Object = MibTableColumn
e7VdslPortCfgUsTargetSnr = _E7VdslPortCfgUsTargetSnr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1, 17),
    _E7VdslPortCfgUsTargetSnr_Type()
)
e7VdslPortCfgUsTargetSnr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgUsTargetSnr.setStatus("current")
if mibBuilder.loadTexts:
    e7VdslPortCfgUsTargetSnr.setUnits("0.1 dB")


class _E7VdslPortCfgPsdMask_Type(Integer32):
    """Custom type e7VdslPortCfgPsdMask based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53)
        )
    )
    namedValues = NamedValues(
        *(("anus0", 1),
          ("aeu32", 2),
          ("aeu36", 3),
          ("aeu40", 4),
          ("aeu44", 5),
          ("aeu48", 6),
          ("aeu52", 7),
          ("aeu56", 8),
          ("aeu60", 9),
          ("aeu64", 10),
          ("aeu128", 11),
          ("aadlu32", 12),
          ("aadlu36", 13),
          ("aadlu40", 14),
          ("aadlu44", 15),
          ("aadlu48", 16),
          ("aadlu52", 17),
          ("aadlu56", 18),
          ("aadlu60", 19),
          ("aadlu64", 20),
          ("aadlu128", 21),
          ("b81", 22),
          ("b82", 23),
          ("b83", 24),
          ("b84", 25),
          ("b85", 26),
          ("b86", 27),
          ("b87", 28),
          ("b88", 29),
          ("b89", 30),
          ("b810", 31),
          ("b811", 32),
          ("b812", 33),
          ("b813", 34),
          ("b814", 35),
          ("b815", 36),
          ("b816", 37),
          ("b71", 38),
          ("b72", 39),
          ("b73", 40),
          ("b74", 41),
          ("b75", 42),
          ("b76", 43),
          ("b77", 44),
          ("b78", 45),
          ("b79", 46),
          ("b710", 47),
          ("c138b", 48),
          ("c276b", 49),
          ("c138co", 50),
          ("c276co", 51),
          ("ctcmisdn", 52),
          ("vdsl1qamcompatible", 53))
    )


_E7VdslPortCfgPsdMask_Type.__name__ = "Integer32"
_E7VdslPortCfgPsdMask_Object = MibTableColumn
e7VdslPortCfgPsdMask = _E7VdslPortCfgPsdMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1, 18),
    _E7VdslPortCfgPsdMask_Type()
)
e7VdslPortCfgPsdMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgPsdMask.setStatus("current")
_E7VdslPortCfgLastTemplate_Type = DisplayString
_E7VdslPortCfgLastTemplate_Object = MibTableColumn
e7VdslPortCfgLastTemplate = _E7VdslPortCfgLastTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 4, 1, 19),
    _E7VdslPortCfgLastTemplate_Type()
)
e7VdslPortCfgLastTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7VdslPortCfgLastTemplate.setStatus("current")
_E7VdslPortCfgTemplateTable_Object = MibTable
e7VdslPortCfgTemplateTable = _E7VdslPortCfgTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5)
)
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateTable.setStatus("current")
_E7VdslPortCfgTemplateEntry_Object = MibTableRow
e7VdslPortCfgTemplateEntry = _E7VdslPortCfgTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1)
)
e7VdslPortCfgTemplateEntry.setIndexNames(
    (0, "E7-Calix-MIB", "e7VdslPortCfgTemplateIndex"),
)
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateEntry.setStatus("current")
_E7VdslPortCfgTemplateIndex_Type = Integer32
_E7VdslPortCfgTemplateIndex_Object = MibTableColumn
e7VdslPortCfgTemplateIndex = _E7VdslPortCfgTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 1),
    _E7VdslPortCfgTemplateIndex_Type()
)
e7VdslPortCfgTemplateIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateIndex.setStatus("current")
_E7VdslPortCfgTemplateName_Type = DisplayString
_E7VdslPortCfgTemplateName_Object = MibTableColumn
e7VdslPortCfgTemplateName = _E7VdslPortCfgTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 2),
    _E7VdslPortCfgTemplateName_Type()
)
e7VdslPortCfgTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateName.setStatus("current")


class _E7VdslPortCfgTemplateServiceType_Type(Integer32):
    """Custom type e7VdslPortCfgTemplateServiceType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("auto", 1),
          ("mm", 2),
          ("mm2plus", 3),
          ("t1413", 4),
          ("gdmt", 5),
          ("glite", 6),
          ("adsl2", 7),
          ("adsl2plus", 8),
          ("readsl2", 9),
          ("annexm", 10),
          ("vdsl2", 11),
          ("vdsl2mm", 12))
    )


_E7VdslPortCfgTemplateServiceType_Type.__name__ = "Integer32"
_E7VdslPortCfgTemplateServiceType_Object = MibTableColumn
e7VdslPortCfgTemplateServiceType = _E7VdslPortCfgTemplateServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 3),
    _E7VdslPortCfgTemplateServiceType_Type()
)
e7VdslPortCfgTemplateServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateServiceType.setStatus("current")


class _E7VdslPortCfgTemplatePathLatency_Type(Integer32):
    """Custom type e7VdslPortCfgTemplatePathLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("fast", 1),
          ("interleaved", 2))
    )


_E7VdslPortCfgTemplatePathLatency_Type.__name__ = "Integer32"
_E7VdslPortCfgTemplatePathLatency_Object = MibTableColumn
e7VdslPortCfgTemplatePathLatency = _E7VdslPortCfgTemplatePathLatency_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 4),
    _E7VdslPortCfgTemplatePathLatency_Type()
)
e7VdslPortCfgTemplatePathLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplatePathLatency.setStatus("current")


class _E7VdslPortCfgTemplateVdslProfile_Type(Integer32):
    """Custom type e7VdslPortCfgTemplateVdslProfile based on Integer32"""
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
        *(("none", 0),
          ("auto", 1),
          ("vdsl8a", 2),
          ("vdsl8b", 3),
          ("vdsl8c", 4),
          ("vdsl8d", 5),
          ("vdsl12a", 6),
          ("vdsl12b", 7),
          ("vdsl17a", 8),
          ("vdsl30a", 9))
    )


_E7VdslPortCfgTemplateVdslProfile_Type.__name__ = "Integer32"
_E7VdslPortCfgTemplateVdslProfile_Object = MibTableColumn
e7VdslPortCfgTemplateVdslProfile = _E7VdslPortCfgTemplateVdslProfile_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 5),
    _E7VdslPortCfgTemplateVdslProfile_Type()
)
e7VdslPortCfgTemplateVdslProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateVdslProfile.setStatus("current")
_E7VdslPortCfgTemplateDsMinRate_Type = Integer32
_E7VdslPortCfgTemplateDsMinRate_Object = MibTableColumn
e7VdslPortCfgTemplateDsMinRate = _E7VdslPortCfgTemplateDsMinRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 6),
    _E7VdslPortCfgTemplateDsMinRate_Type()
)
e7VdslPortCfgTemplateDsMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateDsMinRate.setStatus("current")
_E7VdslPortCfgTemplateDsMaxRate_Type = Integer32
_E7VdslPortCfgTemplateDsMaxRate_Object = MibTableColumn
e7VdslPortCfgTemplateDsMaxRate = _E7VdslPortCfgTemplateDsMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 7),
    _E7VdslPortCfgTemplateDsMaxRate_Type()
)
e7VdslPortCfgTemplateDsMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateDsMaxRate.setStatus("current")
_E7VdslPortCfgTemplateUsMinRate_Type = Integer32
_E7VdslPortCfgTemplateUsMinRate_Object = MibTableColumn
e7VdslPortCfgTemplateUsMinRate = _E7VdslPortCfgTemplateUsMinRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 8),
    _E7VdslPortCfgTemplateUsMinRate_Type()
)
e7VdslPortCfgTemplateUsMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateUsMinRate.setStatus("current")
_E7VdslPortCfgTemplateUsMaxRate_Type = Integer32
_E7VdslPortCfgTemplateUsMaxRate_Object = MibTableColumn
e7VdslPortCfgTemplateUsMaxRate = _E7VdslPortCfgTemplateUsMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 9),
    _E7VdslPortCfgTemplateUsMaxRate_Type()
)
e7VdslPortCfgTemplateUsMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateUsMaxRate.setStatus("current")


class _E7VdslPortCfgTemplateDsMinInp_Type(Integer32):
    """Custom type e7VdslPortCfgTemplateDsMinInp based on Integer32"""
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
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("none", 1),
          ("halfSym", 2),
          ("oneSym", 3),
          ("twoSym", 4),
          ("threeSym", 5),
          ("fourSym", 6),
          ("fiveSym", 7),
          ("sixSym", 8),
          ("sevenSym", 9),
          ("eightSym", 10),
          ("nineSym", 11),
          ("tenSym", 12),
          ("elevenSym", 13),
          ("twelveSym", 14),
          ("thirteenSym", 15),
          ("fourteenSym", 16),
          ("fifteenSym", 17),
          ("sixteenSym", 18))
    )


_E7VdslPortCfgTemplateDsMinInp_Type.__name__ = "Integer32"
_E7VdslPortCfgTemplateDsMinInp_Object = MibTableColumn
e7VdslPortCfgTemplateDsMinInp = _E7VdslPortCfgTemplateDsMinInp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 10),
    _E7VdslPortCfgTemplateDsMinInp_Type()
)
e7VdslPortCfgTemplateDsMinInp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateDsMinInp.setStatus("current")


class _E7VdslPortCfgTemplateUsMinInp_Type(Integer32):
    """Custom type e7VdslPortCfgTemplateUsMinInp based on Integer32"""
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
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("none", 1),
          ("halfSym", 2),
          ("oneSym", 3),
          ("twoSym", 4),
          ("threeSym", 5),
          ("fourSym", 6),
          ("fiveSym", 7),
          ("sixSym", 8),
          ("sevenSym", 9),
          ("eightSym", 10),
          ("nineSym", 11),
          ("tenSym", 12),
          ("elevenSym", 13),
          ("twelveSym", 14),
          ("thirteenSym", 15),
          ("fourteenSym", 16),
          ("fifteenSym", 17),
          ("sixteenSym", 18))
    )


_E7VdslPortCfgTemplateUsMinInp_Type.__name__ = "Integer32"
_E7VdslPortCfgTemplateUsMinInp_Object = MibTableColumn
e7VdslPortCfgTemplateUsMinInp = _E7VdslPortCfgTemplateUsMinInp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 11),
    _E7VdslPortCfgTemplateUsMinInp_Type()
)
e7VdslPortCfgTemplateUsMinInp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateUsMinInp.setStatus("current")
_E7VdslPortCfgTemplateDsInterleaveMaxLatency_Type = Integer32
_E7VdslPortCfgTemplateDsInterleaveMaxLatency_Object = MibTableColumn
e7VdslPortCfgTemplateDsInterleaveMaxLatency = _E7VdslPortCfgTemplateDsInterleaveMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 12),
    _E7VdslPortCfgTemplateDsInterleaveMaxLatency_Type()
)
e7VdslPortCfgTemplateDsInterleaveMaxLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateDsInterleaveMaxLatency.setStatus("current")
_E7VdslPortCfgTemplateUsInterleaveMaxLatency_Type = Integer32
_E7VdslPortCfgTemplateUsInterleaveMaxLatency_Object = MibTableColumn
e7VdslPortCfgTemplateUsInterleaveMaxLatency = _E7VdslPortCfgTemplateUsInterleaveMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 13),
    _E7VdslPortCfgTemplateUsInterleaveMaxLatency_Type()
)
e7VdslPortCfgTemplateUsInterleaveMaxLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateUsInterleaveMaxLatency.setStatus("current")
_E7VdslPortCfgTemplateDsMinSnr_Type = Integer32
_E7VdslPortCfgTemplateDsMinSnr_Object = MibTableColumn
e7VdslPortCfgTemplateDsMinSnr = _E7VdslPortCfgTemplateDsMinSnr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 14),
    _E7VdslPortCfgTemplateDsMinSnr_Type()
)
e7VdslPortCfgTemplateDsMinSnr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateDsMinSnr.setStatus("current")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateDsMinSnr.setUnits("0.1 dB")
_E7VdslPortCfgTemplateDsMaxSnr_Type = Integer32
_E7VdslPortCfgTemplateDsMaxSnr_Object = MibTableColumn
e7VdslPortCfgTemplateDsMaxSnr = _E7VdslPortCfgTemplateDsMaxSnr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 15),
    _E7VdslPortCfgTemplateDsMaxSnr_Type()
)
e7VdslPortCfgTemplateDsMaxSnr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateDsMaxSnr.setStatus("current")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateDsMaxSnr.setUnits("0.1 dB")
_E7VdslPortCfgTemplateDsTargetSnr_Type = Integer32
_E7VdslPortCfgTemplateDsTargetSnr_Object = MibTableColumn
e7VdslPortCfgTemplateDsTargetSnr = _E7VdslPortCfgTemplateDsTargetSnr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 16),
    _E7VdslPortCfgTemplateDsTargetSnr_Type()
)
e7VdslPortCfgTemplateDsTargetSnr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateDsTargetSnr.setStatus("current")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateDsTargetSnr.setUnits("0.1 dB")
_E7VdslPortCfgTemplateUsMinSnr_Type = Integer32
_E7VdslPortCfgTemplateUsMinSnr_Object = MibTableColumn
e7VdslPortCfgTemplateUsMinSnr = _E7VdslPortCfgTemplateUsMinSnr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 17),
    _E7VdslPortCfgTemplateUsMinSnr_Type()
)
e7VdslPortCfgTemplateUsMinSnr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateUsMinSnr.setStatus("current")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateUsMinSnr.setUnits("0.1 dB")
_E7VdslPortCfgTemplateUsMaxSnr_Type = Integer32
_E7VdslPortCfgTemplateUsMaxSnr_Object = MibTableColumn
e7VdslPortCfgTemplateUsMaxSnr = _E7VdslPortCfgTemplateUsMaxSnr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 18),
    _E7VdslPortCfgTemplateUsMaxSnr_Type()
)
e7VdslPortCfgTemplateUsMaxSnr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateUsMaxSnr.setStatus("current")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateUsMaxSnr.setUnits("0.1 dB")
_E7VdslPortCfgTemplateUsTargetSnr_Type = Integer32
_E7VdslPortCfgTemplateUsTargetSnr_Object = MibTableColumn
e7VdslPortCfgTemplateUsTargetSnr = _E7VdslPortCfgTemplateUsTargetSnr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 19),
    _E7VdslPortCfgTemplateUsTargetSnr_Type()
)
e7VdslPortCfgTemplateUsTargetSnr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateUsTargetSnr.setStatus("current")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplateUsTargetSnr.setUnits("0.1 dB")


class _E7VdslPortCfgTemplatePsdMask_Type(Integer32):
    """Custom type e7VdslPortCfgTemplatePsdMask based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53)
        )
    )
    namedValues = NamedValues(
        *(("anus0", 1),
          ("aeu32", 2),
          ("aeu36", 3),
          ("aeu40", 4),
          ("aeu44", 5),
          ("aeu48", 6),
          ("aeu52", 7),
          ("aeu56", 8),
          ("aeu60", 9),
          ("aeu64", 10),
          ("aeu128", 11),
          ("aadlu32", 12),
          ("aadlu36", 13),
          ("aadlu40", 14),
          ("aadlu44", 15),
          ("aadlu48", 16),
          ("aadlu52", 17),
          ("aadlu56", 18),
          ("aadlu60", 19),
          ("aadlu64", 20),
          ("aadlu128", 21),
          ("b81", 22),
          ("b82", 23),
          ("b83", 24),
          ("b84", 25),
          ("b85", 26),
          ("b86", 27),
          ("b87", 28),
          ("b88", 29),
          ("b89", 30),
          ("b810", 31),
          ("b811", 32),
          ("b812", 33),
          ("b813", 34),
          ("b814", 35),
          ("b815", 36),
          ("b816", 37),
          ("b71", 38),
          ("b72", 39),
          ("b73", 40),
          ("b74", 41),
          ("b75", 42),
          ("b76", 43),
          ("b77", 44),
          ("b78", 45),
          ("b79", 46),
          ("b710", 47),
          ("c138b", 48),
          ("c276b", 49),
          ("c138co", 50),
          ("c276co", 51),
          ("ctcmisdn", 52),
          ("vdsl1qamcompatible", 53))
    )


_E7VdslPortCfgTemplatePsdMask_Type.__name__ = "Integer32"
_E7VdslPortCfgTemplatePsdMask_Object = MibTableColumn
e7VdslPortCfgTemplatePsdMask = _E7VdslPortCfgTemplatePsdMask_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 5, 1, 20),
    _E7VdslPortCfgTemplatePsdMask_Type()
)
e7VdslPortCfgTemplatePsdMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e7VdslPortCfgTemplatePsdMask.setStatus("current")
_E7VdslPortPerfIntervalTable_Object = MibTable
e7VdslPortPerfIntervalTable = _E7VdslPortPerfIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 6)
)
if mibBuilder.loadTexts:
    e7VdslPortPerfIntervalTable.setStatus("current")
_E7VdslPortPerfIntervalEntry_Object = MibTableRow
e7VdslPortPerfIntervalEntry = _E7VdslPortPerfIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 6, 1)
)
e7VdslPortPerfIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "E7-Calix-MIB", "e7VdslPortPerfIntervalPhysSide"),
    (0, "E7-Calix-MIB", "e7VdslPortPerfIntervalNumber"),
)
if mibBuilder.loadTexts:
    e7VdslPortPerfIntervalEntry.setStatus("current")
_E7VdslPortPerfIntervalPhysSide_Type = Integer32
_E7VdslPortPerfIntervalPhysSide_Object = MibTableColumn
e7VdslPortPerfIntervalPhysSide = _E7VdslPortPerfIntervalPhysSide_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 6, 1, 1),
    _E7VdslPortPerfIntervalPhysSide_Type()
)
e7VdslPortPerfIntervalPhysSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7VdslPortPerfIntervalPhysSide.setStatus("current")
_E7VdslPortPerfIntervalNumber_Type = Integer32
_E7VdslPortPerfIntervalNumber_Object = MibTableColumn
e7VdslPortPerfIntervalNumber = _E7VdslPortPerfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 6, 1, 2),
    _E7VdslPortPerfIntervalNumber_Type()
)
e7VdslPortPerfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7VdslPortPerfIntervalNumber.setStatus("current")
_E7VdslPortPerfIntervalUAS_Type = Integer32
_E7VdslPortPerfIntervalUAS_Object = MibTableColumn
e7VdslPortPerfIntervalUAS = _E7VdslPortPerfIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 9, 1, 6, 1, 3),
    _E7VdslPortPerfIntervalUAS_Type()
)
e7VdslPortPerfIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7VdslPortPerfIntervalUAS.setStatus("current")
_E7OntGroup_ObjectIdentity = ObjectIdentity
e7OntGroup = _E7OntGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 10)
)
_E7OntTable_Object = MibTable
e7OntTable = _E7OntTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    e7OntTable.setStatus("current")
_E7OntEntry_Object = MibTableRow
e7OntEntry = _E7OntEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 10, 1, 1)
)
e7OntEntry.setIndexNames(
    (0, "E7-Calix-MIB", "e7OntUnitId"),
)
if mibBuilder.loadTexts:
    e7OntEntry.setStatus("current")
_E7OntUnitId_Type = Integer32
_E7OntUnitId_Object = MibTableColumn
e7OntUnitId = _E7OntUnitId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 10, 1, 1, 1),
    _E7OntUnitId_Type()
)
e7OntUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e7OntUnitId.setStatus("current")
_E7OntRowStatus_Type = RowStatus
_E7OntRowStatus_Object = MibTableColumn
e7OntRowStatus = _E7OntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 10, 1, 1, 2),
    _E7OntRowStatus_Type()
)
e7OntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7OntRowStatus.setStatus("current")
_E7OntAdminStatus_Type = E7AdminStatus
_E7OntAdminStatus_Object = MibTableColumn
e7OntAdminStatus = _E7OntAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 10, 1, 1, 3),
    _E7OntAdminStatus_Type()
)
e7OntAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    e7OntAdminStatus.setStatus("current")


class _E7OntOperStatus_Type(Integer32):
    """Custom type e7OntOperStatus based on Integer32"""
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
        *(("invalid", 0),
          ("enabled", 1),
          ("degraded", 2),
          ("systemDisabled", 3),
          ("userDisabled", 4),
          ("waitRegistration", 5))
    )


_E7OntOperStatus_Type.__name__ = "Integer32"
_E7OntOperStatus_Object = MibTableColumn
e7OntOperStatus = _E7OntOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 10, 1, 1, 4),
    _E7OntOperStatus_Type()
)
e7OntOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7OntOperStatus.setStatus("current")


class _E7OntDyingGasp_Type(Integer32):
    """Custom type e7OntDyingGasp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_E7OntDyingGasp_Type.__name__ = "Integer32"
_E7OntDyingGasp_Object = MibTableColumn
e7OntDyingGasp = _E7OntDyingGasp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 10, 1, 1, 5),
    _E7OntDyingGasp_Type()
)
e7OntDyingGasp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7OntDyingGasp.setStatus("current")
_E7OntRxOpticalLevel_Type = Integer32
_E7OntRxOpticalLevel_Object = MibTableColumn
e7OntRxOpticalLevel = _E7OntRxOpticalLevel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 10, 1, 1, 6),
    _E7OntRxOpticalLevel_Type()
)
e7OntRxOpticalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7OntRxOpticalLevel.setStatus("current")
if mibBuilder.loadTexts:
    e7OntRxOpticalLevel.setUnits("0.002 dBm")
_E7OntTxOpticalLevel_Type = Integer32
_E7OntTxOpticalLevel_Object = MibTableColumn
e7OntTxOpticalLevel = _E7OntTxOpticalLevel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 10, 1, 1, 7),
    _E7OntTxOpticalLevel_Type()
)
e7OntTxOpticalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7OntTxOpticalLevel.setStatus("current")
if mibBuilder.loadTexts:
    e7OntTxOpticalLevel.setUnits("0.002 dBm")
_E7OntFarEndRxOpticalLevel_Type = Integer32
_E7OntFarEndRxOpticalLevel_Object = MibTableColumn
e7OntFarEndRxOpticalLevel = _E7OntFarEndRxOpticalLevel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 10, 1, 1, 8),
    _E7OntFarEndRxOpticalLevel_Type()
)
e7OntFarEndRxOpticalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7OntFarEndRxOpticalLevel.setStatus("current")
if mibBuilder.loadTexts:
    e7OntFarEndRxOpticalLevel.setUnits("0.002 dBm")
_E7OntSoftwareVersion_Type = OctetString
_E7OntSoftwareVersion_Object = MibTableColumn
e7OntSoftwareVersion = _E7OntSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 10, 1, 1, 9),
    _E7OntSoftwareVersion_Type()
)
e7OntSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7OntSoftwareVersion.setStatus("current")
_E7OntCleiCode_Type = OctetString
_E7OntCleiCode_Object = MibTableColumn
e7OntCleiCode = _E7OntCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 10, 1, 1, 10),
    _E7OntCleiCode_Type()
)
e7OntCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e7OntCleiCode.setStatus("current")
_E7LaserGroup_ObjectIdentity = ObjectIdentity
e7LaserGroup = _E7LaserGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 2, 2, 1, 14)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "E7-Calix-MIB",
    **{"e7ResourceModule": e7ResourceModule,
       "e7Resource": e7Resource,
       "e7NodeResource": e7NodeResource,
       "e7CraftGroup": e7CraftGroup,
       "e7CraftUserGroup": e7CraftUserGroup,
       "e7CardGroup": e7CardGroup,
       "e7CardTable": e7CardTable,
       "e7CardEntry": e7CardEntry,
       "e7CardBank": e7CardBank,
       "e7CardIndex": e7CardIndex,
       "e7CardRowStatus": e7CardRowStatus,
       "e7CardAdminStatus": e7CardAdminStatus,
       "e7CardProvType": e7CardProvType,
       "e7CardActualType": e7CardActualType,
       "e7CardSoftwareVersion": e7CardSoftwareVersion,
       "e7CardSerialNumber": e7CardSerialNumber,
       "e7CardCurrentPowerLevel": e7CardCurrentPowerLevel,
       "e7CardCleiCode": e7CardCleiCode,
       "e7CardPartNumber": e7CardPartNumber,
       "e7CardStartMacRange": e7CardStartMacRange,
       "e7CardEndMacRange": e7CardEndMacRange,
       "e7OltPonPortTable": e7OltPonPortTable,
       "e7OltPonPortEntry": e7OltPonPortEntry,
       "e7OltPonPortShelf": e7OltPonPortShelf,
       "e7OltPonPortSlot": e7OltPonPortSlot,
       "e7OltPonPortId": e7OltPonPortId,
       "e7OltPonPortStatus": e7OltPonPortStatus,
       "e7OltPonPortTemperature": e7OltPonPortTemperature,
       "e7OltPonPortTxBias": e7OltPonPortTxBias,
       "e7OltPonPortTxPower": e7OltPonPortTxPower,
       "e7OltPonPortRxPower": e7OltPonPortRxPower,
       "e7OltPonPortVoltage": e7OltPonPortVoltage,
       "e7SystemGroup": e7SystemGroup,
       "e7SystemId": e7SystemId,
       "e7SystemLocation": e7SystemLocation,
       "e7SystemAutoUpgrade": e7SystemAutoUpgrade,
       "e7SystemTelnetServer": e7SystemTelnetServer,
       "e7SystemUnsecuredWeb": e7SystemUnsecuredWeb,
       "e7SystemPasswordExpiry": e7SystemPasswordExpiry,
       "e7SystemDnsPrimary": e7SystemDnsPrimary,
       "e7SystemDnsSecondary": e7SystemDnsSecondary,
       "e7SystemTimezone": e7SystemTimezone,
       "e7SystemChassisSerialNumber": e7SystemChassisSerialNumber,
       "e7SystemChassisMacAddress": e7SystemChassisMacAddress,
       "e7SystemTime": e7SystemTime,
       "e7SystemDate": e7SystemDate,
       "e7PortGroup": e7PortGroup,
       "e7VdslPortGroup": e7VdslPortGroup,
       "e7VdslPortTable": e7VdslPortTable,
       "e7VdslPortEntry": e7VdslPortEntry,
       "e7VdslPortRowStatus": e7VdslPortRowStatus,
       "e7VdslPortAdminStatus": e7VdslPortAdminStatus,
       "e7VdslPortCurrTxRate": e7VdslPortCurrTxRate,
       "e7VdslPortCurrRxRate": e7VdslPortCurrRxRate,
       "e7VdslPortStatsProtocol": e7VdslPortStatsProtocol,
       "e7VdslPortLineState": e7VdslPortLineState,
       "e7VdslRateTable": e7VdslRateTable,
       "e7VdslRateEntry": e7VdslRateEntry,
       "e7VdslRateRowStatus": e7VdslRateRowStatus,
       "e7VdslRateAdminStatus": e7VdslRateAdminStatus,
       "e7VdslRateProvDataRateUs": e7VdslRateProvDataRateUs,
       "e7VdslRateProvDataRateDs": e7VdslRateProvDataRateDs,
       "e7VdslPhysTable": e7VdslPhysTable,
       "e7VdslPhysEntry": e7VdslPhysEntry,
       "e7VdslPhysSide": e7VdslPhysSide,
       "e7VdslPhysCurrSnrMargin": e7VdslPhysCurrSnrMargin,
       "e7VdslPhysCurrAtn": e7VdslPhysCurrAtn,
       "e7VdslPhysCurrOutputPwr": e7VdslPhysCurrOutputPwr,
       "e7VdslPhysInterleaveDelay": e7VdslPhysInterleaveDelay,
       "e7VdslPhysImpulseNoiseProtection": e7VdslPhysImpulseNoiseProtection,
       "e7VdslPhysTransmissionMode": e7VdslPhysTransmissionMode,
       "e7VdslPortCfgTable": e7VdslPortCfgTable,
       "e7VdslPortCfgEntry": e7VdslPortCfgEntry,
       "e7VdslPortCfgServiceType": e7VdslPortCfgServiceType,
       "e7VdslPortCfgPathLatency": e7VdslPortCfgPathLatency,
       "e7VdslPortCfgVdslProfile": e7VdslPortCfgVdslProfile,
       "e7VdslPortCfgDsMinRate": e7VdslPortCfgDsMinRate,
       "e7VdslPortCfgDsMaxRate": e7VdslPortCfgDsMaxRate,
       "e7VdslPortCfgUsMinRate": e7VdslPortCfgUsMinRate,
       "e7VdslPortCfgUsMaxRate": e7VdslPortCfgUsMaxRate,
       "e7VdslPortCfgDsMinInp": e7VdslPortCfgDsMinInp,
       "e7VdslPortCfgUsMinInp": e7VdslPortCfgUsMinInp,
       "e7VdslPortCfgDsInterleaveMaxLatency": e7VdslPortCfgDsInterleaveMaxLatency,
       "e7VdslPortCfgUsInterleaveMaxLatency": e7VdslPortCfgUsInterleaveMaxLatency,
       "e7VdslPortCfgDsMinSnr": e7VdslPortCfgDsMinSnr,
       "e7VdslPortCfgDsMaxSnr": e7VdslPortCfgDsMaxSnr,
       "e7VdslPortCfgDsTargetSnr": e7VdslPortCfgDsTargetSnr,
       "e7VdslPortCfgUsMinSnr": e7VdslPortCfgUsMinSnr,
       "e7VdslPortCfgUsMaxSnr": e7VdslPortCfgUsMaxSnr,
       "e7VdslPortCfgUsTargetSnr": e7VdslPortCfgUsTargetSnr,
       "e7VdslPortCfgPsdMask": e7VdslPortCfgPsdMask,
       "e7VdslPortCfgLastTemplate": e7VdslPortCfgLastTemplate,
       "e7VdslPortCfgTemplateTable": e7VdslPortCfgTemplateTable,
       "e7VdslPortCfgTemplateEntry": e7VdslPortCfgTemplateEntry,
       "e7VdslPortCfgTemplateIndex": e7VdslPortCfgTemplateIndex,
       "e7VdslPortCfgTemplateName": e7VdslPortCfgTemplateName,
       "e7VdslPortCfgTemplateServiceType": e7VdslPortCfgTemplateServiceType,
       "e7VdslPortCfgTemplatePathLatency": e7VdslPortCfgTemplatePathLatency,
       "e7VdslPortCfgTemplateVdslProfile": e7VdslPortCfgTemplateVdslProfile,
       "e7VdslPortCfgTemplateDsMinRate": e7VdslPortCfgTemplateDsMinRate,
       "e7VdslPortCfgTemplateDsMaxRate": e7VdslPortCfgTemplateDsMaxRate,
       "e7VdslPortCfgTemplateUsMinRate": e7VdslPortCfgTemplateUsMinRate,
       "e7VdslPortCfgTemplateUsMaxRate": e7VdslPortCfgTemplateUsMaxRate,
       "e7VdslPortCfgTemplateDsMinInp": e7VdslPortCfgTemplateDsMinInp,
       "e7VdslPortCfgTemplateUsMinInp": e7VdslPortCfgTemplateUsMinInp,
       "e7VdslPortCfgTemplateDsInterleaveMaxLatency": e7VdslPortCfgTemplateDsInterleaveMaxLatency,
       "e7VdslPortCfgTemplateUsInterleaveMaxLatency": e7VdslPortCfgTemplateUsInterleaveMaxLatency,
       "e7VdslPortCfgTemplateDsMinSnr": e7VdslPortCfgTemplateDsMinSnr,
       "e7VdslPortCfgTemplateDsMaxSnr": e7VdslPortCfgTemplateDsMaxSnr,
       "e7VdslPortCfgTemplateDsTargetSnr": e7VdslPortCfgTemplateDsTargetSnr,
       "e7VdslPortCfgTemplateUsMinSnr": e7VdslPortCfgTemplateUsMinSnr,
       "e7VdslPortCfgTemplateUsMaxSnr": e7VdslPortCfgTemplateUsMaxSnr,
       "e7VdslPortCfgTemplateUsTargetSnr": e7VdslPortCfgTemplateUsTargetSnr,
       "e7VdslPortCfgTemplatePsdMask": e7VdslPortCfgTemplatePsdMask,
       "e7VdslPortPerfIntervalTable": e7VdslPortPerfIntervalTable,
       "e7VdslPortPerfIntervalEntry": e7VdslPortPerfIntervalEntry,
       "e7VdslPortPerfIntervalPhysSide": e7VdslPortPerfIntervalPhysSide,
       "e7VdslPortPerfIntervalNumber": e7VdslPortPerfIntervalNumber,
       "e7VdslPortPerfIntervalUAS": e7VdslPortPerfIntervalUAS,
       "e7OntGroup": e7OntGroup,
       "e7OntTable": e7OntTable,
       "e7OntEntry": e7OntEntry,
       "e7OntUnitId": e7OntUnitId,
       "e7OntRowStatus": e7OntRowStatus,
       "e7OntAdminStatus": e7OntAdminStatus,
       "e7OntOperStatus": e7OntOperStatus,
       "e7OntDyingGasp": e7OntDyingGasp,
       "e7OntRxOpticalLevel": e7OntRxOpticalLevel,
       "e7OntTxOpticalLevel": e7OntTxOpticalLevel,
       "e7OntFarEndRxOpticalLevel": e7OntFarEndRxOpticalLevel,
       "e7OntSoftwareVersion": e7OntSoftwareVersion,
       "e7OntCleiCode": e7OntCleiCode,
       "e7LaserGroup": e7LaserGroup}
)
