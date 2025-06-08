# SNMP MIB module (RJ45IOC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/softib_52861/RJ45IOC-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:02:53 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sibrj45ioc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52861, 1)
)
if mibBuilder.loadTexts:
    sibrj45ioc.setRevisions(
        ("2018-10-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Softib_ObjectIdentity = ObjectIdentity
softib = _Softib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52861)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52861, 1, 1)
)


class _Name_Type(DisplayString):
    """Custom type name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Name_Type.__name__ = "DisplayString"
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 52861, 1, 1, 1),
    _Name_Type()
)
name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    name.setStatus("current")
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 52861, 1, 1, 2),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_Date_Type = DisplayString
_Date_Object = MibScalar
date = _Date_Object(
    (1, 3, 6, 1, 4, 1, 52861, 1, 1, 3),
    _Date_Type()
)
date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    date.setStatus("current")
_Code_Type = DisplayString
_Code_Object = MibScalar
code = _Code_Object(
    (1, 3, 6, 1, 4, 1, 52861, 1, 1, 4),
    _Code_Type()
)
code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    code.setStatus("current")
_Ports_ObjectIdentity = ObjectIdentity
ports = _Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52861, 1, 2)
)
_IoPortsTable_Object = MibTable
ioPortsTable = _IoPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 52861, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ioPortsTable.setStatus("current")
_IoPortsTableEntry_Object = MibTableRow
ioPortsTableEntry = _IoPortsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52861, 1, 2, 1, 1)
)
ioPortsTableEntry.setIndexNames(
    (0, "RJ45IOC-MIB", "ioPortNumber"),
)
if mibBuilder.loadTexts:
    ioPortsTableEntry.setStatus("current")


class _IoPortNumber_Type(Integer32):
    """Custom type ioPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_IoPortNumber_Type.__name__ = "Integer32"
_IoPortNumber_Object = MibTableColumn
ioPortNumber = _IoPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52861, 1, 2, 1, 1, 1),
    _IoPortNumber_Type()
)
ioPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ioPortNumber.setStatus("current")


class _IoPortName_Type(DisplayString):
    """Custom type ioPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_IoPortName_Type.__name__ = "DisplayString"
_IoPortName_Object = MibTableColumn
ioPortName = _IoPortName_Object(
    (1, 3, 6, 1, 4, 1, 52861, 1, 2, 1, 1, 2),
    _IoPortName_Type()
)
ioPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioPortName.setStatus("current")


class _IoPortType_Type(Integer32):
    """Custom type ioPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_IoPortType_Type.__name__ = "Integer32"
_IoPortType_Object = MibTableColumn
ioPortType = _IoPortType_Object(
    (1, 3, 6, 1, 4, 1, 52861, 1, 2, 1, 1, 3),
    _IoPortType_Type()
)
ioPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioPortType.setStatus("current")


class _IoPortValue_Type(Integer32):
    """Custom type ioPortValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_IoPortValue_Type.__name__ = "Integer32"
_IoPortValue_Object = MibTableColumn
ioPortValue = _IoPortValue_Object(
    (1, 3, 6, 1, 4, 1, 52861, 1, 2, 1, 1, 4),
    _IoPortValue_Type()
)
ioPortValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioPortValue.setStatus("current")


class _IoPortTrap_Type(Integer32):
    """Custom type ioPortTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_IoPortTrap_Type.__name__ = "Integer32"
_IoPortTrap_Object = MibTableColumn
ioPortTrap = _IoPortTrap_Object(
    (1, 3, 6, 1, 4, 1, 52861, 1, 2, 1, 1, 5),
    _IoPortTrap_Type()
)
ioPortTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioPortTrap.setStatus("current")
_Sensors_ObjectIdentity = ObjectIdentity
sensors = _Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52861, 1, 3)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52861, 1, 4)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52861, 1, 5)
)

# Managed Objects groups

snmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52861, 1, 5, 1)
)
snmpGroup.setObjects(
      *(("RJ45IOC-MIB", "name"),
        ("RJ45IOC-MIB", "version"),
        ("RJ45IOC-MIB", "date"),
        ("RJ45IOC-MIB", "code"))
)
if mibBuilder.loadTexts:
    snmpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RJ45IOC-MIB",
    **{"softib": softib,
       "sibrj45ioc": sibrj45ioc,
       "device": device,
       "name": name,
       "version": version,
       "date": date,
       "code": code,
       "ports": ports,
       "ioPortsTable": ioPortsTable,
       "ioPortsTableEntry": ioPortsTableEntry,
       "ioPortNumber": ioPortNumber,
       "ioPortName": ioPortName,
       "ioPortType": ioPortType,
       "ioPortValue": ioPortValue,
       "ioPortTrap": ioPortTrap,
       "sensors": sensors,
       "traps": traps,
       "groups": groups,
       "snmpGroup": snmpGroup}
)
