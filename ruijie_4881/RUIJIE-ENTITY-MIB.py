# SNMP MIB module (RUIJIE-ENTITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-ENTITY-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:21 2025
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

(entPhysicalName,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalName")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruijieEntityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21)
)
if mibBuilder.loadTexts:
    ruijieEntityMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieDeviceMIBObjects_ObjectIdentity = ObjectIdentity
ruijieDeviceMIBObjects = _RuijieDeviceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1)
)
_RuijieDeviceMaxNumber_Type = Integer32
_RuijieDeviceMaxNumber_Object = MibScalar
ruijieDeviceMaxNumber = _RuijieDeviceMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 1),
    _RuijieDeviceMaxNumber_Type()
)
ruijieDeviceMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceMaxNumber.setStatus("current")
_RuijieDeviceInfoTable_Object = MibTable
ruijieDeviceInfoTable = _RuijieDeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieDeviceInfoTable.setStatus("current")
_RuijieDeviceInfoEntry_Object = MibTableRow
ruijieDeviceInfoEntry = _RuijieDeviceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1)
)
ruijieDeviceInfoEntry.setIndexNames(
    (0, "RUIJIE-ENTITY-MIB", "ruijieDeviceInfoIndex"),
)
if mibBuilder.loadTexts:
    ruijieDeviceInfoEntry.setStatus("current")
_RuijieDeviceInfoIndex_Type = Integer32
_RuijieDeviceInfoIndex_Object = MibTableColumn
ruijieDeviceInfoIndex = _RuijieDeviceInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 1),
    _RuijieDeviceInfoIndex_Type()
)
ruijieDeviceInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceInfoIndex.setStatus("current")


class _RuijieDeviceInfoDescr_Type(DisplayString):
    """Custom type ruijieDeviceInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieDeviceInfoDescr_Type.__name__ = "DisplayString"
_RuijieDeviceInfoDescr_Object = MibTableColumn
ruijieDeviceInfoDescr = _RuijieDeviceInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 2),
    _RuijieDeviceInfoDescr_Type()
)
ruijieDeviceInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceInfoDescr.setStatus("current")
_RuijieDeviceInfoSlotNumber_Type = Integer32
_RuijieDeviceInfoSlotNumber_Object = MibTableColumn
ruijieDeviceInfoSlotNumber = _RuijieDeviceInfoSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 3),
    _RuijieDeviceInfoSlotNumber_Type()
)
ruijieDeviceInfoSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceInfoSlotNumber.setStatus("current")


class _RuijieDevicePowerStatus_Type(Integer32):
    """Custom type ruijieDevicePowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("rpsNoLink", 1),
          ("rpsLinkAndNoPower", 2),
          ("rpsLinkAndReadyForPower", 3),
          ("rpsLinkAndPower", 4))
    )


_RuijieDevicePowerStatus_Type.__name__ = "Integer32"
_RuijieDevicePowerStatus_Object = MibTableColumn
ruijieDevicePowerStatus = _RuijieDevicePowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 4),
    _RuijieDevicePowerStatus_Type()
)
ruijieDevicePowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDevicePowerStatus.setStatus("current")
_RuijieDeviceMacAddress_Type = MacAddress
_RuijieDeviceMacAddress_Object = MibTableColumn
ruijieDeviceMacAddress = _RuijieDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 5),
    _RuijieDeviceMacAddress_Type()
)
ruijieDeviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceMacAddress.setStatus("current")


class _RuijieDevicePriority_Type(Integer32):
    """Custom type ruijieDevicePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RuijieDevicePriority_Type.__name__ = "Integer32"
_RuijieDevicePriority_Object = MibTableColumn
ruijieDevicePriority = _RuijieDevicePriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 6),
    _RuijieDevicePriority_Type()
)
ruijieDevicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDevicePriority.setStatus("current")


class _RuijieDeviceAlias_Type(DisplayString):
    """Custom type ruijieDeviceAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieDeviceAlias_Type.__name__ = "DisplayString"
_RuijieDeviceAlias_Object = MibTableColumn
ruijieDeviceAlias = _RuijieDeviceAlias_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 7),
    _RuijieDeviceAlias_Type()
)
ruijieDeviceAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieDeviceAlias.setStatus("current")


class _RuijieDeviceSWVersion_Type(DisplayString):
    """Custom type ruijieDeviceSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieDeviceSWVersion_Type.__name__ = "DisplayString"
_RuijieDeviceSWVersion_Object = MibTableColumn
ruijieDeviceSWVersion = _RuijieDeviceSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 8),
    _RuijieDeviceSWVersion_Type()
)
ruijieDeviceSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceSWVersion.setStatus("current")


class _RuijieDeviceHWVersion_Type(DisplayString):
    """Custom type ruijieDeviceHWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieDeviceHWVersion_Type.__name__ = "DisplayString"
_RuijieDeviceHWVersion_Object = MibTableColumn
ruijieDeviceHWVersion = _RuijieDeviceHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 9),
    _RuijieDeviceHWVersion_Type()
)
ruijieDeviceHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceHWVersion.setStatus("current")


class _RuijieDeviceSerialNumber_Type(DisplayString):
    """Custom type ruijieDeviceSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieDeviceSerialNumber_Type.__name__ = "DisplayString"
_RuijieDeviceSerialNumber_Object = MibTableColumn
ruijieDeviceSerialNumber = _RuijieDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 10),
    _RuijieDeviceSerialNumber_Type()
)
ruijieDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceSerialNumber.setStatus("current")
_RuijieDeviceOid_Type = ObjectIdentifier
_RuijieDeviceOid_Object = MibTableColumn
ruijieDeviceOid = _RuijieDeviceOid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 2, 1, 11),
    _RuijieDeviceOid_Type()
)
ruijieDeviceOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieDeviceOid.setStatus("current")
_RuijieSlotInfoTable_Object = MibTable
ruijieSlotInfoTable = _RuijieSlotInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieSlotInfoTable.setStatus("current")
_RuijieSlotInfoEntry_Object = MibTableRow
ruijieSlotInfoEntry = _RuijieSlotInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1)
)
ruijieSlotInfoEntry.setIndexNames(
    (0, "RUIJIE-ENTITY-MIB", "ruijieSlotInfoDeviceIndex"),
    (0, "RUIJIE-ENTITY-MIB", "ruijieSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    ruijieSlotInfoEntry.setStatus("current")
_RuijieSlotInfoDeviceIndex_Type = Integer32
_RuijieSlotInfoDeviceIndex_Object = MibTableColumn
ruijieSlotInfoDeviceIndex = _RuijieSlotInfoDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 1),
    _RuijieSlotInfoDeviceIndex_Type()
)
ruijieSlotInfoDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotInfoDeviceIndex.setStatus("current")
_RuijieSlotInfoIndex_Type = Integer32
_RuijieSlotInfoIndex_Object = MibTableColumn
ruijieSlotInfoIndex = _RuijieSlotInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 2),
    _RuijieSlotInfoIndex_Type()
)
ruijieSlotInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotInfoIndex.setStatus("current")
_RuijieSlotModuleInfoDescr_Type = DisplayString
_RuijieSlotModuleInfoDescr_Object = MibTableColumn
ruijieSlotModuleInfoDescr = _RuijieSlotModuleInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 3),
    _RuijieSlotModuleInfoDescr_Type()
)
ruijieSlotModuleInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotModuleInfoDescr.setStatus("current")
_RuijieSlotInfoPortNumber_Type = Integer32
_RuijieSlotInfoPortNumber_Object = MibTableColumn
ruijieSlotInfoPortNumber = _RuijieSlotInfoPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 4),
    _RuijieSlotInfoPortNumber_Type()
)
ruijieSlotInfoPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotInfoPortNumber.setStatus("current")
_RuijieSlotInfoPortMaxNumber_Type = Integer32
_RuijieSlotInfoPortMaxNumber_Object = MibTableColumn
ruijieSlotInfoPortMaxNumber = _RuijieSlotInfoPortMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 5),
    _RuijieSlotInfoPortMaxNumber_Type()
)
ruijieSlotInfoPortMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotInfoPortMaxNumber.setStatus("current")


class _RuijieSlotInfoDesc_Type(DisplayString):
    """Custom type ruijieSlotInfoDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieSlotInfoDesc_Type.__name__ = "DisplayString"
_RuijieSlotInfoDesc_Object = MibTableColumn
ruijieSlotInfoDesc = _RuijieSlotInfoDesc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 6),
    _RuijieSlotInfoDesc_Type()
)
ruijieSlotInfoDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotInfoDesc.setStatus("current")


class _RuijieSlotConfigModuleInfoDescr_Type(DisplayString):
    """Custom type ruijieSlotConfigModuleInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieSlotConfigModuleInfoDescr_Type.__name__ = "DisplayString"
_RuijieSlotConfigModuleInfoDescr_Object = MibTableColumn
ruijieSlotConfigModuleInfoDescr = _RuijieSlotConfigModuleInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 7),
    _RuijieSlotConfigModuleInfoDescr_Type()
)
ruijieSlotConfigModuleInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotConfigModuleInfoDescr.setStatus("current")
_RuijieSlotUserStatus_Type = Integer32
_RuijieSlotUserStatus_Object = MibTableColumn
ruijieSlotUserStatus = _RuijieSlotUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 8),
    _RuijieSlotUserStatus_Type()
)
ruijieSlotUserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotUserStatus.setStatus("current")
_RuijieSlotSoftwareStatus_Type = Integer32
_RuijieSlotSoftwareStatus_Object = MibTableColumn
ruijieSlotSoftwareStatus = _RuijieSlotSoftwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 9),
    _RuijieSlotSoftwareStatus_Type()
)
ruijieSlotSoftwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotSoftwareStatus.setStatus("current")


class _RuijieSlotSerialNumber_Type(DisplayString):
    """Custom type ruijieSlotSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieSlotSerialNumber_Type.__name__ = "DisplayString"
_RuijieSlotSerialNumber_Object = MibTableColumn
ruijieSlotSerialNumber = _RuijieSlotSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 10),
    _RuijieSlotSerialNumber_Type()
)
ruijieSlotSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotSerialNumber.setStatus("current")


class _RuijieSlotHWVersion_Type(DisplayString):
    """Custom type ruijieSlotHWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieSlotHWVersion_Type.__name__ = "DisplayString"
_RuijieSlotHWVersion_Object = MibTableColumn
ruijieSlotHWVersion = _RuijieSlotHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 11),
    _RuijieSlotHWVersion_Type()
)
ruijieSlotHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotHWVersion.setStatus("current")


class _RuijieSlotSoftwareVersion_Type(DisplayString):
    """Custom type ruijieSlotSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieSlotSoftwareVersion_Type.__name__ = "DisplayString"
_RuijieSlotSoftwareVersion_Object = MibTableColumn
ruijieSlotSoftwareVersion = _RuijieSlotSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 12),
    _RuijieSlotSoftwareVersion_Type()
)
ruijieSlotSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotSoftwareVersion.setStatus("current")


class _RuijieSlotServiceState_Type(Integer32):
    """Custom type ruijieSlotServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2),
          ("servNA", 3))
    )


_RuijieSlotServiceState_Type.__name__ = "Integer32"
_RuijieSlotServiceState_Object = MibTableColumn
ruijieSlotServiceState = _RuijieSlotServiceState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 3, 1, 13),
    _RuijieSlotServiceState_Type()
)
ruijieSlotServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSlotServiceState.setStatus("current")
_RuijieModuleTempStateTable_Object = MibTable
ruijieModuleTempStateTable = _RuijieModuleTempStateTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieModuleTempStateTable.setStatus("current")
_RuijieModuleTempStateEntry_Object = MibTableRow
ruijieModuleTempStateEntry = _RuijieModuleTempStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 4, 1)
)
ruijieModuleTempStateEntry.setIndexNames(
    (0, "RUIJIE-ENTITY-MIB", "ruijieModuleTempStateDeviceIndex"),
    (0, "RUIJIE-ENTITY-MIB", "ruijieModuleTempStateIndex"),
)
if mibBuilder.loadTexts:
    ruijieModuleTempStateEntry.setStatus("current")
_RuijieModuleTempStateDeviceIndex_Type = Integer32
_RuijieModuleTempStateDeviceIndex_Object = MibTableColumn
ruijieModuleTempStateDeviceIndex = _RuijieModuleTempStateDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 4, 1, 1),
    _RuijieModuleTempStateDeviceIndex_Type()
)
ruijieModuleTempStateDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieModuleTempStateDeviceIndex.setStatus("current")
_RuijieModuleTempStateIndex_Type = Integer32
_RuijieModuleTempStateIndex_Object = MibTableColumn
ruijieModuleTempStateIndex = _RuijieModuleTempStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 4, 1, 2),
    _RuijieModuleTempStateIndex_Type()
)
ruijieModuleTempStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieModuleTempStateIndex.setStatus("current")


class _RuijieModuleTempState_Type(Integer32):
    """Custom type ruijieModuleTempState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tempNormal", 1),
          ("tempWarning", 2))
    )


_RuijieModuleTempState_Type.__name__ = "Integer32"
_RuijieModuleTempState_Object = MibTableColumn
ruijieModuleTempState = _RuijieModuleTempState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 4, 1, 3),
    _RuijieModuleTempState_Type()
)
ruijieModuleTempState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieModuleTempState.setStatus("current")
_RuijiePowerStateTable_Object = MibTable
ruijiePowerStateTable = _RuijiePowerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 5)
)
if mibBuilder.loadTexts:
    ruijiePowerStateTable.setStatus("current")
_RuijiePowerStateEntry_Object = MibTableRow
ruijiePowerStateEntry = _RuijiePowerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 5, 1)
)
ruijiePowerStateEntry.setIndexNames(
    (0, "RUIJIE-ENTITY-MIB", "ruijiePowerStateDeviceIndex"),
    (0, "RUIJIE-ENTITY-MIB", "ruijiePowerStateIndex"),
)
if mibBuilder.loadTexts:
    ruijiePowerStateEntry.setStatus("current")
_RuijiePowerStateDeviceIndex_Type = Integer32
_RuijiePowerStateDeviceIndex_Object = MibTableColumn
ruijiePowerStateDeviceIndex = _RuijiePowerStateDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 5, 1, 1),
    _RuijiePowerStateDeviceIndex_Type()
)
ruijiePowerStateDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePowerStateDeviceIndex.setStatus("current")
_RuijiePowerStateIndex_Type = Integer32
_RuijiePowerStateIndex_Object = MibTableColumn
ruijiePowerStateIndex = _RuijiePowerStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 5, 1, 2),
    _RuijiePowerStateIndex_Type()
)
ruijiePowerStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePowerStateIndex.setStatus("current")


class _RuijiePowerState_Type(Integer32):
    """Custom type ruijiePowerState based on Integer32"""
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
        *(("noLink", 1),
          ("linkAndNoPower", 2),
          ("linkAndReadyForPower", 3),
          ("linkAndPower", 4),
          ("linkAndPowerAbnormal", 5))
    )


_RuijiePowerState_Type.__name__ = "Integer32"
_RuijiePowerState_Object = MibTableColumn
ruijiePowerState = _RuijiePowerState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 5, 1, 3),
    _RuijiePowerState_Type()
)
ruijiePowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePowerState.setStatus("current")


class _RuijiePowerStatePowerDescr_Type(DisplayString):
    """Custom type ruijiePowerStatePowerDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijiePowerStatePowerDescr_Type.__name__ = "DisplayString"
_RuijiePowerStatePowerDescr_Object = MibTableColumn
ruijiePowerStatePowerDescr = _RuijiePowerStatePowerDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 5, 1, 4),
    _RuijiePowerStatePowerDescr_Type()
)
ruijiePowerStatePowerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePowerStatePowerDescr.setStatus("current")


class _RuijiePowerStateSerialNumber_Type(DisplayString):
    """Custom type ruijiePowerStateSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijiePowerStateSerialNumber_Type.__name__ = "DisplayString"
_RuijiePowerStateSerialNumber_Object = MibTableColumn
ruijiePowerStateSerialNumber = _RuijiePowerStateSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 5, 1, 5),
    _RuijiePowerStateSerialNumber_Type()
)
ruijiePowerStateSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePowerStateSerialNumber.setStatus("current")
_RuijieFanStateTable_Object = MibTable
ruijieFanStateTable = _RuijieFanStateTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieFanStateTable.setStatus("current")
_RuijieFanStateEntry_Object = MibTableRow
ruijieFanStateEntry = _RuijieFanStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 6, 1)
)
ruijieFanStateEntry.setIndexNames(
    (0, "RUIJIE-ENTITY-MIB", "ruijieFanStateDeviceIndex"),
    (0, "RUIJIE-ENTITY-MIB", "ruijieFanStateIndex"),
)
if mibBuilder.loadTexts:
    ruijieFanStateEntry.setStatus("current")
_RuijieFanStateDeviceIndex_Type = Integer32
_RuijieFanStateDeviceIndex_Object = MibTableColumn
ruijieFanStateDeviceIndex = _RuijieFanStateDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 6, 1, 1),
    _RuijieFanStateDeviceIndex_Type()
)
ruijieFanStateDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFanStateDeviceIndex.setStatus("current")
_RuijieFanStateIndex_Type = Integer32
_RuijieFanStateIndex_Object = MibTableColumn
ruijieFanStateIndex = _RuijieFanStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 6, 1, 2),
    _RuijieFanStateIndex_Type()
)
ruijieFanStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFanStateIndex.setStatus("current")


class _RuijieFanState_Type(Integer32):
    """Custom type ruijieFanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("work", 1),
          ("stop", 2))
    )


_RuijieFanState_Type.__name__ = "Integer32"
_RuijieFanState_Object = MibTableColumn
ruijieFanState = _RuijieFanState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 6, 1, 3),
    _RuijieFanState_Type()
)
ruijieFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFanState.setStatus("current")


class _RuijieFanStateFanDescr_Type(DisplayString):
    """Custom type ruijieFanStateFanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieFanStateFanDescr_Type.__name__ = "DisplayString"
_RuijieFanStateFanDescr_Object = MibTableColumn
ruijieFanStateFanDescr = _RuijieFanStateFanDescr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 6, 1, 4),
    _RuijieFanStateFanDescr_Type()
)
ruijieFanStateFanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFanStateFanDescr.setStatus("current")


class _RuijieFanStateSerialNumber_Type(DisplayString):
    """Custom type ruijieFanStateSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieFanStateSerialNumber_Type.__name__ = "DisplayString"
_RuijieFanStateSerialNumber_Object = MibTableColumn
ruijieFanStateSerialNumber = _RuijieFanStateSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 6, 1, 5),
    _RuijieFanStateSerialNumber_Type()
)
ruijieFanStateSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieFanStateSerialNumber.setStatus("current")
_RuijieHolderInfoTable_Object = MibTable
ruijieHolderInfoTable = _RuijieHolderInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 7)
)
if mibBuilder.loadTexts:
    ruijieHolderInfoTable.setStatus("current")
_RuijieHolderInfoEntry_Object = MibTableRow
ruijieHolderInfoEntry = _RuijieHolderInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 7, 1)
)
ruijieHolderInfoEntry.setIndexNames(
    (0, "RUIJIE-ENTITY-MIB", "ruijieHolderInfoDeviceIndex"),
    (0, "RUIJIE-ENTITY-MIB", "ruijieHolderInfoSlotIndex"),
    (0, "RUIJIE-ENTITY-MIB", "ruijieHolderInfoSubSlotIndex"),
)
if mibBuilder.loadTexts:
    ruijieHolderInfoEntry.setStatus("current")
_RuijieHolderInfoDeviceIndex_Type = Integer32
_RuijieHolderInfoDeviceIndex_Object = MibTableColumn
ruijieHolderInfoDeviceIndex = _RuijieHolderInfoDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 7, 1, 1),
    _RuijieHolderInfoDeviceIndex_Type()
)
ruijieHolderInfoDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHolderInfoDeviceIndex.setStatus("current")
_RuijieHolderInfoSlotIndex_Type = Integer32
_RuijieHolderInfoSlotIndex_Object = MibTableColumn
ruijieHolderInfoSlotIndex = _RuijieHolderInfoSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 7, 1, 2),
    _RuijieHolderInfoSlotIndex_Type()
)
ruijieHolderInfoSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHolderInfoSlotIndex.setStatus("current")
_RuijieHolderInfoSubSlotIndex_Type = Integer32
_RuijieHolderInfoSubSlotIndex_Object = MibTableColumn
ruijieHolderInfoSubSlotIndex = _RuijieHolderInfoSubSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 7, 1, 3),
    _RuijieHolderInfoSubSlotIndex_Type()
)
ruijieHolderInfoSubSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHolderInfoSubSlotIndex.setStatus("current")
_RuijieHolderNumber_Type = Integer32
_RuijieHolderNumber_Object = MibTableColumn
ruijieHolderNumber = _RuijieHolderNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 7, 1, 4),
    _RuijieHolderNumber_Type()
)
ruijieHolderNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHolderNumber.setStatus("current")


class _RuijieHolderState_Type(Integer32):
    """Custom type ruijieHolderState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("installed", 2),
          ("unavailable", 3),
          ("unknown", 4))
    )


_RuijieHolderState_Type.__name__ = "Integer32"
_RuijieHolderState_Object = MibTableColumn
ruijieHolderState = _RuijieHolderState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 7, 1, 5),
    _RuijieHolderState_Type()
)
ruijieHolderState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHolderState.setStatus("current")


class _RuijieHolderType_Type(Integer32):
    """Custom type ruijieHolderType based on Integer32"""
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
        *(("rack", 1),
          ("subRack", 2),
          ("shelf", 3),
          ("subShelf", 4),
          ("slot", 5),
          ("subSlot", 6))
    )


_RuijieHolderType_Type.__name__ = "Integer32"
_RuijieHolderType_Object = MibTableColumn
ruijieHolderType = _RuijieHolderType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 7, 1, 6),
    _RuijieHolderType_Type()
)
ruijieHolderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHolderType.setStatus("current")


class _RuijieHolderName_Type(DisplayString):
    """Custom type ruijieHolderName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieHolderName_Type.__name__ = "DisplayString"
_RuijieHolderName_Object = MibTableColumn
ruijieHolderName = _RuijieHolderName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 1, 7, 1, 7),
    _RuijieHolderName_Type()
)
ruijieHolderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieHolderName.setStatus("current")
_RuijieEntityMIBTraps_ObjectIdentity = ObjectIdentity
ruijieEntityMIBTraps = _RuijieEntityMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2)
)
_RuijieEntityStateChgDesc_Type = DisplayString
_RuijieEntityStateChgDesc_Object = MibScalar
ruijieEntityStateChgDesc = _RuijieEntityStateChgDesc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 1),
    _RuijieEntityStateChgDesc_Type()
)
ruijieEntityStateChgDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieEntityStateChgDesc.setStatus("current")


class _RuijieTemperatureWarningDesc_Type(DisplayString):
    """Custom type ruijieTemperatureWarningDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieTemperatureWarningDesc_Type.__name__ = "DisplayString"
_RuijieTemperatureWarningDesc_Object = MibScalar
ruijieTemperatureWarningDesc = _RuijieTemperatureWarningDesc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 3),
    _RuijieTemperatureWarningDesc_Type()
)
ruijieTemperatureWarningDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieTemperatureWarningDesc.setStatus("current")
_RuijieDeviceMIBConformance_ObjectIdentity = ObjectIdentity
ruijieDeviceMIBConformance = _RuijieDeviceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3)
)
_RuijieDeviceMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieDeviceMIBCompliances = _RuijieDeviceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 1)
)
_RuijieDeviceMIBGroups_ObjectIdentity = ObjectIdentity
ruijieDeviceMIBGroups = _RuijieDeviceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2)
)

# Managed Objects groups

ruijieDeviceInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 1)
)
ruijieDeviceInfoMIBGroup.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieDeviceMaxNumber"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceInfoIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceInfoDescr"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceInfoSlotNumber"),
        ("RUIJIE-ENTITY-MIB", "ruijieDevicePowerStatus"))
)
if mibBuilder.loadTexts:
    ruijieDeviceInfoMIBGroup.setStatus("current")

ruijieOptionalDevInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 2)
)
ruijieOptionalDevInfoMIBGroup.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieDeviceMacAddress"),
        ("RUIJIE-ENTITY-MIB", "ruijieDevicePriority"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceAlias"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceSWVersion"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceHWVersion"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceSerialNumber"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceOid"))
)
if mibBuilder.loadTexts:
    ruijieOptionalDevInfoMIBGroup.setStatus("current")

ruijieModuleInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 3)
)
ruijieModuleInfoMIBGroup.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieSlotInfoDeviceIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotInfoIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotModuleInfoDescr"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotInfoPortNumber"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotInfoPortMaxNumber"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotInfoDesc"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotConfigModuleInfoDescr"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotUserStatus"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotSoftwareStatus"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotSerialNumber"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotHWVersion"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotSoftwareVersion"),
        ("RUIJIE-ENTITY-MIB", "ruijieSlotServiceState"))
)
if mibBuilder.loadTexts:
    ruijieModuleInfoMIBGroup.setStatus("current")

ruijieEntityChgDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 4)
)
ruijieEntityChgDescGroup.setObjects(
    ("RUIJIE-ENTITY-MIB", "ruijieEntityStateChgDesc")
)
if mibBuilder.loadTexts:
    ruijieEntityChgDescGroup.setStatus("current")

ruijieModuleTempStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 6)
)
ruijieModuleTempStateGroup.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieModuleTempStateDeviceIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijieModuleTempStateIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijieModuleTempState"))
)
if mibBuilder.loadTexts:
    ruijieModuleTempStateGroup.setStatus("current")

ruijiePowerStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 7)
)
ruijiePowerStateGroup.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijiePowerStateDeviceIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijiePowerStateIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijiePowerState"),
        ("RUIJIE-ENTITY-MIB", "ruijiePowerStatePowerDescr"))
)
if mibBuilder.loadTexts:
    ruijiePowerStateGroup.setStatus("current")

ruijieFanStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 8)
)
ruijieFanStateGroup.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieFanStateDeviceIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijieFanStateIndex"),
        ("RUIJIE-ENTITY-MIB", "ruijieFanState"),
        ("RUIJIE-ENTITY-MIB", "ruijieFanStateFanDescr"))
)
if mibBuilder.loadTexts:
    ruijieFanStateGroup.setStatus("current")

ruijieTemperatureWarningDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 9)
)
ruijieTemperatureWarningDescGroup.setObjects(
    ("RUIJIE-ENTITY-MIB", "ruijieTemperatureWarningDesc")
)
if mibBuilder.loadTexts:
    ruijieTemperatureWarningDescGroup.setStatus("current")

ruijieHolderInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 11)
)
ruijieHolderInfoGroup.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieHolderNumber"),
        ("RUIJIE-ENTITY-MIB", "ruijieHolderState"),
        ("RUIJIE-ENTITY-MIB", "ruijieHolderType"),
        ("RUIJIE-ENTITY-MIB", "ruijieHolderName"))
)
if mibBuilder.loadTexts:
    ruijieHolderInfoGroup.setStatus("current")


# Notification objects

ruijieEntityStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 2)
)
ruijieEntityStatusChange.setObjects(
    ("RUIJIE-ENTITY-MIB", "ruijieEntityStateChgDesc")
)
if mibBuilder.loadTexts:
    ruijieEntityStatusChange.setStatus(
        "current"
    )

ruijieTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 4)
)
ruijieTemperatureWarning.setObjects(
    ("RUIJIE-ENTITY-MIB", "ruijieTemperatureWarningDesc")
)
if mibBuilder.loadTexts:
    ruijieTemperatureWarning.setStatus(
        "current"
    )

ruijieEntityPhyInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 5)
)
ruijieEntityPhyInsert.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    ruijieEntityPhyInsert.setStatus(
        "current"
    )

ruijieEntityPhyRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 2, 6)
)
ruijieEntityPhyRemove.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    ruijieEntityPhyRemove.setStatus(
        "current"
    )


# Notifications groups

ruijieDeviceMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 5)
)
ruijieDeviceMIBNotificationGroup.setObjects(
    ("RUIJIE-ENTITY-MIB", "ruijieEntityStatusChange")
)
if mibBuilder.loadTexts:
    ruijieDeviceMIBNotificationGroup.setStatus(
        "current"
    )

ruijieTemperatureWarningGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 2, 10)
)
ruijieTemperatureWarningGroup.setObjects(
    ("RUIJIE-ENTITY-MIB", "ruijieTemperatureWarning")
)
if mibBuilder.loadTexts:
    ruijieTemperatureWarningGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijieDeviceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 21, 3, 1, 1)
)
ruijieDeviceMIBCompliance.setObjects(
      *(("RUIJIE-ENTITY-MIB", "ruijieDeviceInfoMIBGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieModuleInfoMIBGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieOptionalDevInfoMIBGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieEntityChgDescGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieDeviceMIBNotificationGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieModuleTempStateGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijiePowerStateGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieFanStateGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieTemperatureWarningDescGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieTemperatureWarningGroup"),
        ("RUIJIE-ENTITY-MIB", "ruijieHolderInfoGroup"))
)
if mibBuilder.loadTexts:
    ruijieDeviceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-ENTITY-MIB",
    **{"ruijieEntityMIB": ruijieEntityMIB,
       "ruijieDeviceMIBObjects": ruijieDeviceMIBObjects,
       "ruijieDeviceMaxNumber": ruijieDeviceMaxNumber,
       "ruijieDeviceInfoTable": ruijieDeviceInfoTable,
       "ruijieDeviceInfoEntry": ruijieDeviceInfoEntry,
       "ruijieDeviceInfoIndex": ruijieDeviceInfoIndex,
       "ruijieDeviceInfoDescr": ruijieDeviceInfoDescr,
       "ruijieDeviceInfoSlotNumber": ruijieDeviceInfoSlotNumber,
       "ruijieDevicePowerStatus": ruijieDevicePowerStatus,
       "ruijieDeviceMacAddress": ruijieDeviceMacAddress,
       "ruijieDevicePriority": ruijieDevicePriority,
       "ruijieDeviceAlias": ruijieDeviceAlias,
       "ruijieDeviceSWVersion": ruijieDeviceSWVersion,
       "ruijieDeviceHWVersion": ruijieDeviceHWVersion,
       "ruijieDeviceSerialNumber": ruijieDeviceSerialNumber,
       "ruijieDeviceOid": ruijieDeviceOid,
       "ruijieSlotInfoTable": ruijieSlotInfoTable,
       "ruijieSlotInfoEntry": ruijieSlotInfoEntry,
       "ruijieSlotInfoDeviceIndex": ruijieSlotInfoDeviceIndex,
       "ruijieSlotInfoIndex": ruijieSlotInfoIndex,
       "ruijieSlotModuleInfoDescr": ruijieSlotModuleInfoDescr,
       "ruijieSlotInfoPortNumber": ruijieSlotInfoPortNumber,
       "ruijieSlotInfoPortMaxNumber": ruijieSlotInfoPortMaxNumber,
       "ruijieSlotInfoDesc": ruijieSlotInfoDesc,
       "ruijieSlotConfigModuleInfoDescr": ruijieSlotConfigModuleInfoDescr,
       "ruijieSlotUserStatus": ruijieSlotUserStatus,
       "ruijieSlotSoftwareStatus": ruijieSlotSoftwareStatus,
       "ruijieSlotSerialNumber": ruijieSlotSerialNumber,
       "ruijieSlotHWVersion": ruijieSlotHWVersion,
       "ruijieSlotSoftwareVersion": ruijieSlotSoftwareVersion,
       "ruijieSlotServiceState": ruijieSlotServiceState,
       "ruijieModuleTempStateTable": ruijieModuleTempStateTable,
       "ruijieModuleTempStateEntry": ruijieModuleTempStateEntry,
       "ruijieModuleTempStateDeviceIndex": ruijieModuleTempStateDeviceIndex,
       "ruijieModuleTempStateIndex": ruijieModuleTempStateIndex,
       "ruijieModuleTempState": ruijieModuleTempState,
       "ruijiePowerStateTable": ruijiePowerStateTable,
       "ruijiePowerStateEntry": ruijiePowerStateEntry,
       "ruijiePowerStateDeviceIndex": ruijiePowerStateDeviceIndex,
       "ruijiePowerStateIndex": ruijiePowerStateIndex,
       "ruijiePowerState": ruijiePowerState,
       "ruijiePowerStatePowerDescr": ruijiePowerStatePowerDescr,
       "ruijiePowerStateSerialNumber": ruijiePowerStateSerialNumber,
       "ruijieFanStateTable": ruijieFanStateTable,
       "ruijieFanStateEntry": ruijieFanStateEntry,
       "ruijieFanStateDeviceIndex": ruijieFanStateDeviceIndex,
       "ruijieFanStateIndex": ruijieFanStateIndex,
       "ruijieFanState": ruijieFanState,
       "ruijieFanStateFanDescr": ruijieFanStateFanDescr,
       "ruijieFanStateSerialNumber": ruijieFanStateSerialNumber,
       "ruijieHolderInfoTable": ruijieHolderInfoTable,
       "ruijieHolderInfoEntry": ruijieHolderInfoEntry,
       "ruijieHolderInfoDeviceIndex": ruijieHolderInfoDeviceIndex,
       "ruijieHolderInfoSlotIndex": ruijieHolderInfoSlotIndex,
       "ruijieHolderInfoSubSlotIndex": ruijieHolderInfoSubSlotIndex,
       "ruijieHolderNumber": ruijieHolderNumber,
       "ruijieHolderState": ruijieHolderState,
       "ruijieHolderType": ruijieHolderType,
       "ruijieHolderName": ruijieHolderName,
       "ruijieEntityMIBTraps": ruijieEntityMIBTraps,
       "ruijieEntityStateChgDesc": ruijieEntityStateChgDesc,
       "ruijieEntityStatusChange": ruijieEntityStatusChange,
       "ruijieTemperatureWarningDesc": ruijieTemperatureWarningDesc,
       "ruijieTemperatureWarning": ruijieTemperatureWarning,
       "ruijieEntityPhyInsert": ruijieEntityPhyInsert,
       "ruijieEntityPhyRemove": ruijieEntityPhyRemove,
       "ruijieDeviceMIBConformance": ruijieDeviceMIBConformance,
       "ruijieDeviceMIBCompliances": ruijieDeviceMIBCompliances,
       "ruijieDeviceMIBCompliance": ruijieDeviceMIBCompliance,
       "ruijieDeviceMIBGroups": ruijieDeviceMIBGroups,
       "ruijieDeviceInfoMIBGroup": ruijieDeviceInfoMIBGroup,
       "ruijieOptionalDevInfoMIBGroup": ruijieOptionalDevInfoMIBGroup,
       "ruijieModuleInfoMIBGroup": ruijieModuleInfoMIBGroup,
       "ruijieEntityChgDescGroup": ruijieEntityChgDescGroup,
       "ruijieDeviceMIBNotificationGroup": ruijieDeviceMIBNotificationGroup,
       "ruijieModuleTempStateGroup": ruijieModuleTempStateGroup,
       "ruijiePowerStateGroup": ruijiePowerStateGroup,
       "ruijieFanStateGroup": ruijieFanStateGroup,
       "ruijieTemperatureWarningDescGroup": ruijieTemperatureWarningDescGroup,
       "ruijieTemperatureWarningGroup": ruijieTemperatureWarningGroup,
       "ruijieHolderInfoGroup": ruijieHolderInfoGroup}
)
