# SNMP MIB module (NETSKOPE-APPLIANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/netskope_48007/NETSKOPE-APPLIANCE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:42:17 2025
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

netskopeApplianceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 48007, 6)
)
if mibBuilder.loadTexts:
    netskopeApplianceMIB.setRevisions(
        ("2000-06-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetskopeAppliance_ObjectIdentity = ObjectIdentity
netskopeAppliance = _NetskopeAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48007)
)
_NetskopeApplianceMIBNotifs_ObjectIdentity = ObjectIdentity
netskopeApplianceMIBNotifs = _NetskopeApplianceMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48007, 6, 0)
)
_NetskopeApplianceMIBNotifsGroups_ObjectIdentity = ObjectIdentity
netskopeApplianceMIBNotifsGroups = _NetskopeApplianceMIBNotifsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48007, 6, 1)
)
_NetskopeApplianceMIBObjects_ObjectIdentity = ObjectIdentity
netskopeApplianceMIBObjects = _NetskopeApplianceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48007, 6, 2)
)


class _EnabledServices_Type(OctetString):
    """Custom type enabledServices based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_EnabledServices_Type.__name__ = "OctetString"
_EnabledServices_Object = MibScalar
enabledServices = _EnabledServices_Object(
    (1, 3, 6, 1, 4, 1, 48007, 6, 2, 1),
    _EnabledServices_Type()
)
enabledServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enabledServices.setStatus("current")


class _DataplaneStatus_Type(Integer32):
    """Custom type dataplaneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1),
          ("unknown", 2))
    )


_DataplaneStatus_Type.__name__ = "Integer32"
_DataplaneStatus_Object = MibScalar
dataplaneStatus = _DataplaneStatus_Object(
    (1, 3, 6, 1, 4, 1, 48007, 6, 2, 2),
    _DataplaneStatus_Type()
)
dataplaneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataplaneStatus.setStatus("current")


class _ManagementplaneStatus_Type(Integer32):
    """Custom type managementplaneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1),
          ("onbox", 2),
          ("unknown", 3))
    )


_ManagementplaneStatus_Type.__name__ = "Integer32"
_ManagementplaneStatus_Object = MibScalar
managementplaneStatus = _ManagementplaneStatus_Object(
    (1, 3, 6, 1, 4, 1, 48007, 6, 2, 3),
    _ManagementplaneStatus_Type()
)
managementplaneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementplaneStatus.setStatus("current")


class _LastConnectedToMP_Type(OctetString):
    """Custom type lastConnectedToMP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LastConnectedToMP_Type.__name__ = "OctetString"
_LastConnectedToMP_Object = MibScalar
lastConnectedToMP = _LastConnectedToMP_Object(
    (1, 3, 6, 1, 4, 1, 48007, 6, 2, 4),
    _LastConnectedToMP_Type()
)
lastConnectedToMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastConnectedToMP.setStatus("current")


class _DeviceStatus_Type(Integer32):
    """Custom type deviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 0),
          ("bad", 1),
          ("unknown", 2))
    )


_DeviceStatus_Type.__name__ = "Integer32"
_DeviceStatus_Object = MibScalar
deviceStatus = _DeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 48007, 6, 2, 5),
    _DeviceStatus_Type()
)
deviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceStatus.setStatus("current")
_NetskopeApplianceMIBGroups_ObjectIdentity = ObjectIdentity
netskopeApplianceMIBGroups = _NetskopeApplianceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48007, 6, 3)
)
_NetskopeApplianceMIBConformance_ObjectIdentity = ObjectIdentity
netskopeApplianceMIBConformance = _NetskopeApplianceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48007, 6, 4)
)
_NetskopeApplianceMIBCompliances_ObjectIdentity = ObjectIdentity
netskopeApplianceMIBCompliances = _NetskopeApplianceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48007, 6, 4, 1)
)

# Managed Objects groups

netskopeApplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48007, 6, 3, 1)
)
netskopeApplianceGroup.setObjects(
      *(("NETSKOPE-APPLIANCE-MIB", "enabledServices"),
        ("NETSKOPE-APPLIANCE-MIB", "dataplaneStatus"),
        ("NETSKOPE-APPLIANCE-MIB", "managementplaneStatus"),
        ("NETSKOPE-APPLIANCE-MIB", "lastConnectedToMP"),
        ("NETSKOPE-APPLIANCE-MIB", "deviceStatus"))
)
if mibBuilder.loadTexts:
    netskopeApplianceGroup.setStatus("current")


# Notification objects

mpConnectionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 48007, 6, 0, 1)
)
if mibBuilder.loadTexts:
    mpConnectionNotif.setStatus(
        "current"
    )

deviceStatusNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 48007, 6, 0, 2)
)
if mibBuilder.loadTexts:
    deviceStatusNotif.setStatus(
        "current"
    )


# Notifications groups

netskopeApplianceNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 48007, 6, 1, 1)
)
netskopeApplianceNotifGroup.setObjects(
      *(("NETSKOPE-APPLIANCE-MIB", "mpConnectionNotif"),
        ("NETSKOPE-APPLIANCE-MIB", "deviceStatusNotif"))
)
if mibBuilder.loadTexts:
    netskopeApplianceNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

netskopeApplianceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 48007, 6, 4, 1, 1)
)
netskopeApplianceMIBCompliance.setObjects(
      *(("NETSKOPE-APPLIANCE-MIB", "netskopeApplianceGroup"),
        ("NETSKOPE-APPLIANCE-MIB", "netskopeApplianceNotifGroup"))
)
if mibBuilder.loadTexts:
    netskopeApplianceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSKOPE-APPLIANCE-MIB",
    **{"netskopeAppliance": netskopeAppliance,
       "netskopeApplianceMIB": netskopeApplianceMIB,
       "netskopeApplianceMIBNotifs": netskopeApplianceMIBNotifs,
       "mpConnectionNotif": mpConnectionNotif,
       "deviceStatusNotif": deviceStatusNotif,
       "netskopeApplianceMIBNotifsGroups": netskopeApplianceMIBNotifsGroups,
       "netskopeApplianceNotifGroup": netskopeApplianceNotifGroup,
       "netskopeApplianceMIBObjects": netskopeApplianceMIBObjects,
       "enabledServices": enabledServices,
       "dataplaneStatus": dataplaneStatus,
       "managementplaneStatus": managementplaneStatus,
       "lastConnectedToMP": lastConnectedToMP,
       "deviceStatus": deviceStatus,
       "netskopeApplianceMIBGroups": netskopeApplianceMIBGroups,
       "netskopeApplianceGroup": netskopeApplianceGroup,
       "netskopeApplianceMIBConformance": netskopeApplianceMIBConformance,
       "netskopeApplianceMIBCompliances": netskopeApplianceMIBCompliances,
       "netskopeApplianceMIBCompliance": netskopeApplianceMIBCompliance}
)
