# SNMP MIB module (ME1200-SSH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-SSH-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:31 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

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

me1200SshMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 49)
)
if mibBuilder.loadTexts:
    me1200SshMib.setRevisions(
        ("2014-01-29 00:00",
         "2013-10-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Me1200SshMIBObjects_ObjectIdentity = ObjectIdentity
me1200SshMIBObjects = _Me1200SshMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 49, 1)
)
_Me1200SshConfig_ObjectIdentity = ObjectIdentity
me1200SshConfig = _Me1200SshConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 49, 1, 2)
)
_Me1200SshGlobals_ObjectIdentity = ObjectIdentity
me1200SshGlobals = _Me1200SshGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 49, 1, 2, 1)
)
_Me1200SshGlobalsAdminState_Type = TruthValue
_Me1200SshGlobalsAdminState_Object = MibScalar
me1200SshGlobalsAdminState = _Me1200SshGlobalsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 49, 1, 2, 1, 1),
    _Me1200SshGlobalsAdminState_Type()
)
me1200SshGlobalsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SshGlobalsAdminState.setStatus("current")
_Me1200SshMIBConformance_ObjectIdentity = ObjectIdentity
me1200SshMIBConformance = _Me1200SshMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 49, 2)
)
_Me1200SshMIBCompliances_ObjectIdentity = ObjectIdentity
me1200SshMIBCompliances = _Me1200SshMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 49, 2, 1)
)
_Me1200SshMIBGroups_ObjectIdentity = ObjectIdentity
me1200SshMIBGroups = _Me1200SshMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 49, 2, 2)
)

# Managed Objects groups

me1200SshGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 49, 2, 2, 1)
)
me1200SshGlobalsInfoGroup.setObjects(
    ("ME1200-SSH-MIB", "me1200SshGlobalsAdminState")
)
if mibBuilder.loadTexts:
    me1200SshGlobalsInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200SshMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 49, 2, 1, 1)
)
me1200SshMibCompliance.setObjects(
    ("ME1200-SSH-MIB", "me1200SshGlobalsInfoGroup")
)
if mibBuilder.loadTexts:
    me1200SshMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-SSH-MIB",
    **{"me1200SshMib": me1200SshMib,
       "me1200SshMIBObjects": me1200SshMIBObjects,
       "me1200SshConfig": me1200SshConfig,
       "me1200SshGlobals": me1200SshGlobals,
       "me1200SshGlobalsAdminState": me1200SshGlobalsAdminState,
       "me1200SshMIBConformance": me1200SshMIBConformance,
       "me1200SshMIBCompliances": me1200SshMIBCompliances,
       "me1200SshMibCompliance": me1200SshMibCompliance,
       "me1200SshMIBGroups": me1200SshMIBGroups,
       "me1200SshGlobalsInfoGroup": me1200SshGlobalsInfoGroup}
)
