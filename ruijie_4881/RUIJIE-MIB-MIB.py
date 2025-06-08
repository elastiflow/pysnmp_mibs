# SNMP MIB module (RUIJIE-MIB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-VSD-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:00 2025
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

ruijieVSDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129)
)
if mibBuilder.loadTexts:
    ruijieVSDMIB.setRevisions(
        ("2014-04-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieVSDMIBObjects_ObjectIdentity = ObjectIdentity
ruijieVSDMIBObjects = _RuijieVSDMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1)
)
_RuijieVSDSupport_Type = Integer32
_RuijieVSDSupport_Object = MibScalar
ruijieVSDSupport = _RuijieVSDSupport_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 1),
    _RuijieVSDSupport_Type()
)
ruijieVSDSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDSupport.setStatus("current")
_RuijieVSDCurrentID_Type = Integer32
_RuijieVSDCurrentID_Object = MibScalar
ruijieVSDCurrentID = _RuijieVSDCurrentID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 2),
    _RuijieVSDCurrentID_Type()
)
ruijieVSDCurrentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDCurrentID.setStatus("current")
_RuijieVSDMaxNumber_Type = Integer32
_RuijieVSDMaxNumber_Object = MibScalar
ruijieVSDMaxNumber = _RuijieVSDMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 3),
    _RuijieVSDMaxNumber_Type()
)
ruijieVSDMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDMaxNumber.setStatus("current")
_RuijieVSDCurrentNumber_Type = Integer32
_RuijieVSDCurrentNumber_Object = MibScalar
ruijieVSDCurrentNumber = _RuijieVSDCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 4),
    _RuijieVSDCurrentNumber_Type()
)
ruijieVSDCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDCurrentNumber.setStatus("current")
_RuijieVSDMasterMac_Type = MacAddress
_RuijieVSDMasterMac_Object = MibScalar
ruijieVSDMasterMac = _RuijieVSDMasterMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 5),
    _RuijieVSDMasterMac_Type()
)
ruijieVSDMasterMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDMasterMac.setStatus("current")
_RuijieVSDCurrentMac_Type = MacAddress
_RuijieVSDCurrentMac_Object = MibScalar
ruijieVSDCurrentMac = _RuijieVSDCurrentMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 6),
    _RuijieVSDCurrentMac_Type()
)
ruijieVSDCurrentMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDCurrentMac.setStatus("current")


class _RuijieVSDVituralSerial_Type(DisplayString):
    """Custom type ruijieVSDVituralSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieVSDVituralSerial_Type.__name__ = "DisplayString"
_RuijieVSDVituralSerial_Object = MibScalar
ruijieVSDVituralSerial = _RuijieVSDVituralSerial_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 7),
    _RuijieVSDVituralSerial_Type()
)
ruijieVSDVituralSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDVituralSerial.setStatus("current")


class _RuijieVSDMasterSerial_Type(DisplayString):
    """Custom type ruijieVSDMasterSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieVSDMasterSerial_Type.__name__ = "DisplayString"
_RuijieVSDMasterSerial_Object = MibScalar
ruijieVSDMasterSerial = _RuijieVSDMasterSerial_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 8),
    _RuijieVSDMasterSerial_Type()
)
ruijieVSDMasterSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDMasterSerial.setStatus("current")
_RuijieVSDInfoTable_Object = MibTable
ruijieVSDInfoTable = _RuijieVSDInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 9)
)
if mibBuilder.loadTexts:
    ruijieVSDInfoTable.setStatus("current")
_RuijieVSDInfoEntry_Object = MibTableRow
ruijieVSDInfoEntry = _RuijieVSDInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 9, 1)
)
ruijieVSDInfoEntry.setIndexNames(
    (0, "RUIJIE-MIB-MIB", "ruijieVSDInfoIndex"),
)
if mibBuilder.loadTexts:
    ruijieVSDInfoEntry.setStatus("current")
_RuijieVSDInfoIndex_Type = Integer32
_RuijieVSDInfoIndex_Object = MibTableColumn
ruijieVSDInfoIndex = _RuijieVSDInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 9, 1, 1),
    _RuijieVSDInfoIndex_Type()
)
ruijieVSDInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDInfoIndex.setStatus("current")
_RuijieVSDValid_Type = Integer32
_RuijieVSDValid_Object = MibTableColumn
ruijieVSDValid = _RuijieVSDValid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 9, 1, 2),
    _RuijieVSDValid_Type()
)
ruijieVSDValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDValid.setStatus("current")


class _RuijieVSDName_Type(DisplayString):
    """Custom type ruijieVSDName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieVSDName_Type.__name__ = "DisplayString"
_RuijieVSDName_Object = MibTableColumn
ruijieVSDName = _RuijieVSDName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 9, 1, 3),
    _RuijieVSDName_Type()
)
ruijieVSDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDName.setStatus("current")
_RuijieVSDMacAddress_Type = MacAddress
_RuijieVSDMacAddress_Object = MibTableColumn
ruijieVSDMacAddress = _RuijieVSDMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 9, 1, 4),
    _RuijieVSDMacAddress_Type()
)
ruijieVSDMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDMacAddress.setStatus("current")


class _RuijieVSDSerialNumber_Type(DisplayString):
    """Custom type ruijieVSDSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieVSDSerialNumber_Type.__name__ = "DisplayString"
_RuijieVSDSerialNumber_Object = MibTableColumn
ruijieVSDSerialNumber = _RuijieVSDSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 9, 1, 5),
    _RuijieVSDSerialNumber_Type()
)
ruijieVSDSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDSerialNumber.setStatus("current")


class _RuijieVSDUniqueNumber_Type(DisplayString):
    """Custom type ruijieVSDUniqueNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieVSDUniqueNumber_Type.__name__ = "DisplayString"
_RuijieVSDUniqueNumber_Object = MibTableColumn
ruijieVSDUniqueNumber = _RuijieVSDUniqueNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 9, 1, 6),
    _RuijieVSDUniqueNumber_Type()
)
ruijieVSDUniqueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDUniqueNumber.setStatus("current")
_RuijieVSDPortInfoTable_Object = MibTable
ruijieVSDPortInfoTable = _RuijieVSDPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 10)
)
if mibBuilder.loadTexts:
    ruijieVSDPortInfoTable.setStatus("current")
_RuijieVSDPortInfoEntry_Object = MibTableRow
ruijieVSDPortInfoEntry = _RuijieVSDPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 10, 1)
)
ruijieVSDPortInfoEntry.setIndexNames(
    (0, "RUIJIE-MIB-MIB", "ruijieVSDPortDevice"),
    (0, "RUIJIE-MIB-MIB", "ruijieVSDPortSlot"),
    (0, "RUIJIE-MIB-MIB", "ruijieVSDPortSubslot"),
    (0, "RUIJIE-MIB-MIB", "ruijieVSDPortPortIdx"),
)
if mibBuilder.loadTexts:
    ruijieVSDPortInfoEntry.setStatus("current")
_RuijieVSDPortDevice_Type = Integer32
_RuijieVSDPortDevice_Object = MibTableColumn
ruijieVSDPortDevice = _RuijieVSDPortDevice_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 10, 1, 1),
    _RuijieVSDPortDevice_Type()
)
ruijieVSDPortDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDPortDevice.setStatus("current")
_RuijieVSDPortSlot_Type = Integer32
_RuijieVSDPortSlot_Object = MibTableColumn
ruijieVSDPortSlot = _RuijieVSDPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 10, 1, 2),
    _RuijieVSDPortSlot_Type()
)
ruijieVSDPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDPortSlot.setStatus("current")
_RuijieVSDPortSubslot_Type = Integer32
_RuijieVSDPortSubslot_Object = MibTableColumn
ruijieVSDPortSubslot = _RuijieVSDPortSubslot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 10, 1, 3),
    _RuijieVSDPortSubslot_Type()
)
ruijieVSDPortSubslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDPortSubslot.setStatus("current")
_RuijieVSDPortPortIdx_Type = Integer32
_RuijieVSDPortPortIdx_Object = MibTableColumn
ruijieVSDPortPortIdx = _RuijieVSDPortPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 10, 1, 4),
    _RuijieVSDPortPortIdx_Type()
)
ruijieVSDPortPortIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDPortPortIdx.setStatus("current")
_RuijieVSDPortIfIndex_Type = Integer32
_RuijieVSDPortIfIndex_Object = MibTableColumn
ruijieVSDPortIfIndex = _RuijieVSDPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 10, 1, 5),
    _RuijieVSDPortIfIndex_Type()
)
ruijieVSDPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDPortIfIndex.setStatus("current")
_RuijieVSDPortVSDIndex_Type = Integer32
_RuijieVSDPortVSDIndex_Object = MibTableColumn
ruijieVSDPortVSDIndex = _RuijieVSDPortVSDIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 1, 10, 1, 6),
    _RuijieVSDPortVSDIndex_Type()
)
ruijieVSDPortVSDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVSDPortVSDIndex.setStatus("current")
_RuijieVSDMIBTraps_ObjectIdentity = ObjectIdentity
ruijieVSDMIBTraps = _RuijieVSDMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 2)
)
_RuijieVSDChgDesc_Type = DisplayString
_RuijieVSDChgDesc_Object = MibScalar
ruijieVSDChgDesc = _RuijieVSDChgDesc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 2, 1),
    _RuijieVSDChgDesc_Type()
)
ruijieVSDChgDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieVSDChgDesc.setStatus("current")
_RuijieVSDPortChgDesc_Type = DisplayString
_RuijieVSDPortChgDesc_Object = MibScalar
ruijieVSDPortChgDesc = _RuijieVSDPortChgDesc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 2, 3),
    _RuijieVSDPortChgDesc_Type()
)
ruijieVSDPortChgDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieVSDPortChgDesc.setStatus("current")
_RuijieVSDMIBConformance_ObjectIdentity = ObjectIdentity
ruijieVSDMIBConformance = _RuijieVSDMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 3)
)
_RuijieVSDMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieVSDMIBCompliances = _RuijieVSDMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 3, 1)
)
_RuijieVSDMIBGroups_ObjectIdentity = ObjectIdentity
ruijieVSDMIBGroups = _RuijieVSDMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 3, 2)
)

# Managed Objects groups

ruijieVSDInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 3, 2, 1)
)
ruijieVSDInfoMIBGroup.setObjects(
      *(("RUIJIE-MIB-MIB", "ruijieVSDSupport"),
        ("RUIJIE-MIB-MIB", "ruijieVSDCurrentID"),
        ("RUIJIE-MIB-MIB", "ruijieVSDMaxNumber"),
        ("RUIJIE-MIB-MIB", "ruijieVSDCurrentNumber"),
        ("RUIJIE-MIB-MIB", "ruijieVSDMasterMac"),
        ("RUIJIE-MIB-MIB", "ruijieVSDCurrentMac"),
        ("RUIJIE-MIB-MIB", "ruijieVSDVituralSerial"),
        ("RUIJIE-MIB-MIB", "ruijieVSDMasterSerial"))
)
if mibBuilder.loadTexts:
    ruijieVSDInfoMIBGroup.setStatus("current")

ruijieVSDDetailInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 3, 2, 2)
)
ruijieVSDDetailInfoMIBGroup.setObjects(
      *(("RUIJIE-MIB-MIB", "ruijieVSDInfoIndex"),
        ("RUIJIE-MIB-MIB", "ruijieVSDValid"),
        ("RUIJIE-MIB-MIB", "ruijieVSDName"),
        ("RUIJIE-MIB-MIB", "ruijieVSDMacAddress"),
        ("RUIJIE-MIB-MIB", "ruijieVSDSerialNumber"),
        ("RUIJIE-MIB-MIB", "ruijieVSDUniqueNumber"))
)
if mibBuilder.loadTexts:
    ruijieVSDDetailInfoMIBGroup.setStatus("current")

ruijieVSDPortInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 3, 2, 3)
)
ruijieVSDPortInfoMIBGroup.setObjects(
      *(("RUIJIE-MIB-MIB", "ruijieVSDPortDevice"),
        ("RUIJIE-MIB-MIB", "ruijieVSDPortSlot"),
        ("RUIJIE-MIB-MIB", "ruijieVSDPortSubslot"),
        ("RUIJIE-MIB-MIB", "ruijieVSDPortPortIdx"),
        ("RUIJIE-MIB-MIB", "ruijieVSDPortIfIndex"),
        ("RUIJIE-MIB-MIB", "ruijieVSDPortVSDIndex"))
)
if mibBuilder.loadTexts:
    ruijieVSDPortInfoMIBGroup.setStatus("current")

ruijieVSDChgDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 3, 2, 4)
)
ruijieVSDChgDescGroup.setObjects(
      *(("RUIJIE-MIB-MIB", "ruijieVSDChgDesc"),
        ("RUIJIE-MIB-MIB", "ruijieVSDPortChgDesc"))
)
if mibBuilder.loadTexts:
    ruijieVSDChgDescGroup.setStatus("current")


# Notification objects

ruijieVSDStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 2, 2)
)
ruijieVSDStatusChange.setObjects(
    ("RUIJIE-MIB-MIB", "ruijieVSDChgDesc")
)
if mibBuilder.loadTexts:
    ruijieVSDStatusChange.setStatus(
        "current"
    )

ruijieVSDPortStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 2, 4)
)
ruijieVSDPortStatusChange.setObjects(
    ("RUIJIE-MIB-MIB", "ruijieVSDPortChgDesc")
)
if mibBuilder.loadTexts:
    ruijieVSDPortStatusChange.setStatus(
        "current"
    )


# Notifications groups

ruijieVSDMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 3, 2, 5)
)
ruijieVSDMIBNotificationGroup.setObjects(
      *(("RUIJIE-MIB-MIB", "ruijieVSDStatusChange"),
        ("RUIJIE-MIB-MIB", "ruijieVSDPortStatusChange"))
)
if mibBuilder.loadTexts:
    ruijieVSDMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijieVSDMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 129, 3, 1, 1)
)
ruijieVSDMIBCompliance.setObjects(
      *(("RUIJIE-MIB-MIB", "ruijieVSDInfoMIBGroup"),
        ("RUIJIE-MIB-MIB", "ruijieVSDDetailInfoMIBGroup"),
        ("RUIJIE-MIB-MIB", "ruijieVSDPortInfoMIBGroup"),
        ("RUIJIE-MIB-MIB", "ruijieVSDChgDescGroup"),
        ("RUIJIE-MIB-MIB", "ruijieVSDMIBNotificationGroup"))
)
if mibBuilder.loadTexts:
    ruijieVSDMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-MIB-MIB",
    **{"ruijieVSDMIB": ruijieVSDMIB,
       "ruijieVSDMIBObjects": ruijieVSDMIBObjects,
       "ruijieVSDSupport": ruijieVSDSupport,
       "ruijieVSDCurrentID": ruijieVSDCurrentID,
       "ruijieVSDMaxNumber": ruijieVSDMaxNumber,
       "ruijieVSDCurrentNumber": ruijieVSDCurrentNumber,
       "ruijieVSDMasterMac": ruijieVSDMasterMac,
       "ruijieVSDCurrentMac": ruijieVSDCurrentMac,
       "ruijieVSDVituralSerial": ruijieVSDVituralSerial,
       "ruijieVSDMasterSerial": ruijieVSDMasterSerial,
       "ruijieVSDInfoTable": ruijieVSDInfoTable,
       "ruijieVSDInfoEntry": ruijieVSDInfoEntry,
       "ruijieVSDInfoIndex": ruijieVSDInfoIndex,
       "ruijieVSDValid": ruijieVSDValid,
       "ruijieVSDName": ruijieVSDName,
       "ruijieVSDMacAddress": ruijieVSDMacAddress,
       "ruijieVSDSerialNumber": ruijieVSDSerialNumber,
       "ruijieVSDUniqueNumber": ruijieVSDUniqueNumber,
       "ruijieVSDPortInfoTable": ruijieVSDPortInfoTable,
       "ruijieVSDPortInfoEntry": ruijieVSDPortInfoEntry,
       "ruijieVSDPortDevice": ruijieVSDPortDevice,
       "ruijieVSDPortSlot": ruijieVSDPortSlot,
       "ruijieVSDPortSubslot": ruijieVSDPortSubslot,
       "ruijieVSDPortPortIdx": ruijieVSDPortPortIdx,
       "ruijieVSDPortIfIndex": ruijieVSDPortIfIndex,
       "ruijieVSDPortVSDIndex": ruijieVSDPortVSDIndex,
       "ruijieVSDMIBTraps": ruijieVSDMIBTraps,
       "ruijieVSDChgDesc": ruijieVSDChgDesc,
       "ruijieVSDStatusChange": ruijieVSDStatusChange,
       "ruijieVSDPortChgDesc": ruijieVSDPortChgDesc,
       "ruijieVSDPortStatusChange": ruijieVSDPortStatusChange,
       "ruijieVSDMIBConformance": ruijieVSDMIBConformance,
       "ruijieVSDMIBCompliances": ruijieVSDMIBCompliances,
       "ruijieVSDMIBCompliance": ruijieVSDMIBCompliance,
       "ruijieVSDMIBGroups": ruijieVSDMIBGroups,
       "ruijieVSDInfoMIBGroup": ruijieVSDInfoMIBGroup,
       "ruijieVSDDetailInfoMIBGroup": ruijieVSDDetailInfoMIBGroup,
       "ruijieVSDPortInfoMIBGroup": ruijieVSDPortInfoMIBGroup,
       "ruijieVSDChgDescGroup": ruijieVSDChgDescGroup,
       "ruijieVSDMIBNotificationGroup": ruijieVSDMIBNotificationGroup}
)
