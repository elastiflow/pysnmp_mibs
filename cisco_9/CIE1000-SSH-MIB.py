# SNMP MIB module (CIE1000-SSH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-SSH-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:42 2025
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

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

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

cie1000SshMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49)
)
if mibBuilder.loadTexts:
    cie1000SshMib.setRevisions(
        ("2014-07-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cie1000SshMibObjects_ObjectIdentity = ObjectIdentity
cie1000SshMibObjects = _Cie1000SshMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49, 1)
)
_Cie1000SshConfig_ObjectIdentity = ObjectIdentity
cie1000SshConfig = _Cie1000SshConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49, 1, 2)
)
_Cie1000SshConfigGlobals_ObjectIdentity = ObjectIdentity
cie1000SshConfigGlobals = _Cie1000SshConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49, 1, 2, 1)
)
_Cie1000SshConfigGlobalsAdminState_Type = TruthValue
_Cie1000SshConfigGlobalsAdminState_Object = MibScalar
cie1000SshConfigGlobalsAdminState = _Cie1000SshConfigGlobalsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49, 1, 2, 1, 1),
    _Cie1000SshConfigGlobalsAdminState_Type()
)
cie1000SshConfigGlobalsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SshConfigGlobalsAdminState.setStatus("current")
_Cie1000SshMibConformance_ObjectIdentity = ObjectIdentity
cie1000SshMibConformance = _Cie1000SshMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49, 2)
)
_Cie1000SshMibCompliances_ObjectIdentity = ObjectIdentity
cie1000SshMibCompliances = _Cie1000SshMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49, 2, 1)
)
_Cie1000SshMibGroups_ObjectIdentity = ObjectIdentity
cie1000SshMibGroups = _Cie1000SshMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49, 2, 2)
)

# Managed Objects groups

cie1000SshConfigGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49, 2, 2, 1)
)
cie1000SshConfigGlobalsInfoGroup.setObjects(
    ("CIE1000-SSH-MIB", "cie1000SshConfigGlobalsAdminState")
)
if mibBuilder.loadTexts:
    cie1000SshConfigGlobalsInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000SshMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49, 2, 1, 1)
)
cie1000SshMibCompliance.setObjects(
    ("CIE1000-SSH-MIB", "cie1000SshConfigGlobalsInfoGroup")
)
if mibBuilder.loadTexts:
    cie1000SshMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-SSH-MIB",
    **{"cie1000SshMib": cie1000SshMib,
       "cie1000SshMibObjects": cie1000SshMibObjects,
       "cie1000SshConfig": cie1000SshConfig,
       "cie1000SshConfigGlobals": cie1000SshConfigGlobals,
       "cie1000SshConfigGlobalsAdminState": cie1000SshConfigGlobalsAdminState,
       "cie1000SshMibConformance": cie1000SshMibConformance,
       "cie1000SshMibCompliances": cie1000SshMibCompliances,
       "cie1000SshMibCompliance": cie1000SshMibCompliance,
       "cie1000SshMibGroups": cie1000SshMibGroups,
       "cie1000SshConfigGlobalsInfoGroup": cie1000SshConfigGlobalsInfoGroup}
)
