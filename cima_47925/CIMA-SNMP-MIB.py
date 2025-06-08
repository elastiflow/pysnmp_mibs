# SNMP MIB module (CIMA-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cima_47925/CIMA-SNMP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:50:21 2025
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

cimaSnmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47925)
)
if mibBuilder.loadTexts:
    cimaSnmp.setRevisions(
        ("2016-07-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cima_ObjectIdentity = ObjectIdentity
cima = _Cima_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47925, 1)
)
_CashHandlingDevices_ObjectIdentity = ObjectIdentity
cashHandlingDevices = _CashHandlingDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47925, 1, 1)
)
_BanknoteDevice0_ObjectIdentity = ObjectIdentity
banknoteDevice0 = _BanknoteDevice0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47925, 1, 1, 1)
)


class _Bdm0DeviceProducer_Type(OctetString):
    """Custom type bdm0DeviceProducer based on OctetString"""
    defaultValue = OctetString("Cima S.p.A.")


_Bdm0DeviceProducer_Type.__name__ = "OctetString"
_Bdm0DeviceProducer_Object = MibScalar
bdm0DeviceProducer = _Bdm0DeviceProducer_Object(
    (1, 3, 6, 1, 4, 1, 47925, 1, 1, 1, 1),
    _Bdm0DeviceProducer_Type()
)
bdm0DeviceProducer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdm0DeviceProducer.setStatus("current")


class _Bdm0DeviceModel_Type(OctetString):
    """Custom type bdm0DeviceModel based on OctetString"""
    defaultValue = OctetString("Unknown model")


_Bdm0DeviceModel_Type.__name__ = "OctetString"
_Bdm0DeviceModel_Object = MibScalar
bdm0DeviceModel = _Bdm0DeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 47925, 1, 1, 1, 2),
    _Bdm0DeviceModel_Type()
)
bdm0DeviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdm0DeviceModel.setStatus("current")


class _Bdm0DeviceSerialNumber_Type(OctetString):
    """Custom type bdm0DeviceSerialNumber based on OctetString"""
    defaultValue = OctetString("Cima S.p.A.")


_Bdm0DeviceSerialNumber_Type.__name__ = "OctetString"
_Bdm0DeviceSerialNumber_Object = MibScalar
bdm0DeviceSerialNumber = _Bdm0DeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 47925, 1, 1, 1, 3),
    _Bdm0DeviceSerialNumber_Type()
)
bdm0DeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdm0DeviceSerialNumber.setStatus("current")
_Bdm0DeviceStatusCode_Type = Integer32
_Bdm0DeviceStatusCode_Object = MibScalar
bdm0DeviceStatusCode = _Bdm0DeviceStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 47925, 1, 1, 1, 4),
    _Bdm0DeviceStatusCode_Type()
)
bdm0DeviceStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdm0DeviceStatusCode.setStatus("current")
_CashHandlingDevicesCompliances_ObjectIdentity = ObjectIdentity
cashHandlingDevicesCompliances = _CashHandlingDevicesCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47925, 1, 2)
)
_CashHandlingDevicesGroups_ObjectIdentity = ObjectIdentity
cashHandlingDevicesGroups = _CashHandlingDevicesGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47925, 1, 3)
)

# Managed Objects groups

banknoteDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47925, 1, 3, 1)
)
banknoteDeviceGroup.setObjects(
      *(("CIMA-SNMP-MIB", "bdm0DeviceProducer"),
        ("CIMA-SNMP-MIB", "bdm0DeviceModel"),
        ("CIMA-SNMP-MIB", "bdm0DeviceSerialNumber"),
        ("CIMA-SNMP-MIB", "bdm0DeviceStatusCode"))
)
if mibBuilder.loadTexts:
    banknoteDeviceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

banknoteDeviceComplianceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47925, 1, 2, 1)
)
banknoteDeviceComplianceCompliance.setObjects(
      *(("CIMA-SNMP-MIB", "banknoteDeviceGroup"),
        ("CIMA-SNMP-MIB", "snmpCommunityGroup"))
)
if mibBuilder.loadTexts:
    banknoteDeviceComplianceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIMA-SNMP-MIB",
    **{"cimaSnmp": cimaSnmp,
       "cima": cima,
       "cashHandlingDevices": cashHandlingDevices,
       "banknoteDevice0": banknoteDevice0,
       "bdm0DeviceProducer": bdm0DeviceProducer,
       "bdm0DeviceModel": bdm0DeviceModel,
       "bdm0DeviceSerialNumber": bdm0DeviceSerialNumber,
       "bdm0DeviceStatusCode": bdm0DeviceStatusCode,
       "cashHandlingDevicesCompliances": cashHandlingDevicesCompliances,
       "banknoteDeviceComplianceCompliance": banknoteDeviceComplianceCompliance,
       "cashHandlingDevicesGroups": cashHandlingDevicesGroups,
       "banknoteDeviceGroup": banknoteDeviceGroup}
)
