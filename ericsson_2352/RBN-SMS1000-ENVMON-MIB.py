# SNMP MIB module (RBN-SMS1000-ENVMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2352/RBN-SMS1000-ENVMON-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:10:42 2025
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

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rbnSMS1000EnvMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 3)
)
if mibBuilder.loadTexts:
    rbnSMS1000EnvMonMIB.setRevisions(
        ("2002-05-29 00:00",
         "1999-08-03 23:00",
         "1998-10-06 23:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnSMS1000EnvMonMIBNotifications_ObjectIdentity = ObjectIdentity
rbnSMS1000EnvMonMIBNotifications = _RbnSMS1000EnvMonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 3, 0)
)
_RbnSMS1000EnvMonMIBObjects_ObjectIdentity = ObjectIdentity
rbnSMS1000EnvMonMIBObjects = _RbnSMS1000EnvMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 3, 1)
)
_RbnSMS1000FanFail_Type = TruthValue
_RbnSMS1000FanFail_Object = MibScalar
rbnSMS1000FanFail = _RbnSMS1000FanFail_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 3, 1, 1),
    _RbnSMS1000FanFail_Type()
)
rbnSMS1000FanFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSMS1000FanFail.setStatus("obsolete")
_RbnSMS1000PowerFail_Type = TruthValue
_RbnSMS1000PowerFail_Object = MibScalar
rbnSMS1000PowerFail = _RbnSMS1000PowerFail_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 3, 1, 2),
    _RbnSMS1000PowerFail_Type()
)
rbnSMS1000PowerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSMS1000PowerFail.setStatus("obsolete")
_RbnSMS1000EnvMonMIBConformance_ObjectIdentity = ObjectIdentity
rbnSMS1000EnvMonMIBConformance = _RbnSMS1000EnvMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 3, 2)
)
_RbnSMS1000EnvMonMIBGroups_ObjectIdentity = ObjectIdentity
rbnSMS1000EnvMonMIBGroups = _RbnSMS1000EnvMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 3, 2, 1)
)
_RbnSMS1000EnvMonMIBCompliances_ObjectIdentity = ObjectIdentity
rbnSMS1000EnvMonMIBCompliances = _RbnSMS1000EnvMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 3, 2, 2)
)

# Managed Objects groups

rbnSMS1000EnvMonMIBObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 3, 2, 1, 1)
)
rbnSMS1000EnvMonMIBObjectGroup.setObjects(
      *(("RBN-SMS1000-ENVMON-MIB", "rbnSMS1000FanFail"),
        ("RBN-SMS1000-ENVMON-MIB", "rbnSMS1000PowerFail"))
)
if mibBuilder.loadTexts:
    rbnSMS1000EnvMonMIBObjectGroup.setStatus("obsolete")


# Notification objects

rbnSMS1000FanFailChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 3, 0, 1)
)
rbnSMS1000FanFailChange.setObjects(
    ("RBN-SMS1000-ENVMON-MIB", "rbnSMS1000FanFail")
)
if mibBuilder.loadTexts:
    rbnSMS1000FanFailChange.setStatus(
        "obsolete"
    )

rbnSMS1000PowerFailChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 3, 0, 2)
)
rbnSMS1000PowerFailChange.setObjects(
    ("RBN-SMS1000-ENVMON-MIB", "rbnSMS1000PowerFail")
)
if mibBuilder.loadTexts:
    rbnSMS1000PowerFailChange.setStatus(
        "obsolete"
    )


# Notifications groups

rbnSMS1000EnvMonMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 3, 2, 1, 2)
)
rbnSMS1000EnvMonMIBNotificationGroup.setObjects(
      *(("RBN-SMS1000-ENVMON-MIB", "rbnSMS1000FanFailChange"),
        ("RBN-SMS1000-ENVMON-MIB", "rbnSMS1000PowerFailChange"))
)
if mibBuilder.loadTexts:
    rbnSMS1000EnvMonMIBNotificationGroup.setStatus(
        "obsolete"
    )


# Agent capabilities


# Module compliance

rbnSMS1000EnvMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 3, 2, 2, 1)
)
rbnSMS1000EnvMonMIBCompliance.setObjects(
      *(("RBN-SMS1000-ENVMON-MIB", "rbnSMS1000EnvMonMIBObjectGroup"),
        ("RBN-SMS1000-ENVMON-MIB", "rbnSMS1000EnvMonMIBNotificationGroup"))
)
if mibBuilder.loadTexts:
    rbnSMS1000EnvMonMIBCompliance.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-SMS1000-ENVMON-MIB",
    **{"rbnSMS1000EnvMonMIB": rbnSMS1000EnvMonMIB,
       "rbnSMS1000EnvMonMIBNotifications": rbnSMS1000EnvMonMIBNotifications,
       "rbnSMS1000FanFailChange": rbnSMS1000FanFailChange,
       "rbnSMS1000PowerFailChange": rbnSMS1000PowerFailChange,
       "rbnSMS1000EnvMonMIBObjects": rbnSMS1000EnvMonMIBObjects,
       "rbnSMS1000FanFail": rbnSMS1000FanFail,
       "rbnSMS1000PowerFail": rbnSMS1000PowerFail,
       "rbnSMS1000EnvMonMIBConformance": rbnSMS1000EnvMonMIBConformance,
       "rbnSMS1000EnvMonMIBGroups": rbnSMS1000EnvMonMIBGroups,
       "rbnSMS1000EnvMonMIBObjectGroup": rbnSMS1000EnvMonMIBObjectGroup,
       "rbnSMS1000EnvMonMIBNotificationGroup": rbnSMS1000EnvMonMIBNotificationGroup,
       "rbnSMS1000EnvMonMIBCompliances": rbnSMS1000EnvMonMIBCompliances,
       "rbnSMS1000EnvMonMIBCompliance": rbnSMS1000EnvMonMIBCompliance}
)
