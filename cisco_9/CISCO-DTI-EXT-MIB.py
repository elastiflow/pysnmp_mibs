# SNMP MIB module (CISCO-DTI-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-DTI-EXT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:11:57 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(dtiProtocolClientStatusFlag,
 dtiProtocolServerStatusFlag) = mibBuilder.importSymbols(
    "DTI-MIB",
    "dtiProtocolClientStatusFlag",
    "dtiProtocolServerStatusFlag")

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

ciscoDtiExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 822)
)
if mibBuilder.loadTexts:
    ciscoDtiExtMIB.setRevisions(
        ("2014-08-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDtiExtNotifs_ObjectIdentity = ObjectIdentity
ciscoDtiExtNotifs = _CiscoDtiExtNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 822, 0)
)
_CiscoDtiExtObjects_ObjectIdentity = ObjectIdentity
ciscoDtiExtObjects = _CiscoDtiExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 822, 1)
)


class _CdeServerStatusChangeEnable_Type(TruthValue):
    """Custom type cdeServerStatusChangeEnable based on TruthValue"""
    defaultValue = 2


_CdeServerStatusChangeEnable_Type.__name__ = "TruthValue"
_CdeServerStatusChangeEnable_Object = MibScalar
cdeServerStatusChangeEnable = _CdeServerStatusChangeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 822, 1, 1),
    _CdeServerStatusChangeEnable_Type()
)
cdeServerStatusChangeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeServerStatusChangeEnable.setStatus("current")


class _CdeClientStatusChangeEnable_Type(TruthValue):
    """Custom type cdeClientStatusChangeEnable based on TruthValue"""
    defaultValue = 2


_CdeClientStatusChangeEnable_Type.__name__ = "TruthValue"
_CdeClientStatusChangeEnable_Object = MibScalar
cdeClientStatusChangeEnable = _CdeClientStatusChangeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 822, 1, 2),
    _CdeClientStatusChangeEnable_Type()
)
cdeClientStatusChangeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeClientStatusChangeEnable.setStatus("current")
_CiscoDtiExtConform_ObjectIdentity = ObjectIdentity
ciscoDtiExtConform = _CiscoDtiExtConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 822, 2)
)
_CiscoDtiExtCompliances_ObjectIdentity = ObjectIdentity
ciscoDtiExtCompliances = _CiscoDtiExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 1)
)
_CiscoDtiExtGroups_ObjectIdentity = ObjectIdentity
ciscoDtiExtGroups = _CiscoDtiExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 2)
)

# Managed Objects groups

ciscoDtiExtNotifsControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 2, 1)
)
ciscoDtiExtNotifsControlGroup.setObjects(
      *(("CISCO-DTI-EXT-MIB", "cdeServerStatusChangeEnable"),
        ("CISCO-DTI-EXT-MIB", "cdeClientStatusChangeEnable"))
)
if mibBuilder.loadTexts:
    ciscoDtiExtNotifsControlGroup.setStatus("current")


# Notification objects

cdeServerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 822, 0, 1)
)
cdeServerStatusChange.setObjects(
    ("DTI-MIB", "dtiProtocolServerStatusFlag")
)
if mibBuilder.loadTexts:
    cdeServerStatusChange.setStatus(
        "current"
    )

cdeClientStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 822, 0, 2)
)
cdeClientStatusChange.setObjects(
    ("DTI-MIB", "dtiProtocolClientStatusFlag")
)
if mibBuilder.loadTexts:
    cdeClientStatusChange.setStatus(
        "current"
    )


# Notifications groups

ciscoDtiExtNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 2, 2)
)
ciscoDtiExtNotifsGroup.setObjects(
      *(("CISCO-DTI-EXT-MIB", "cdeServerStatusChange"),
        ("CISCO-DTI-EXT-MIB", "cdeClientStatusChange"))
)
if mibBuilder.loadTexts:
    ciscoDtiExtNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoDtiExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 1, 1)
)
ciscoDtiExtCompliance.setObjects(
      *(("CISCO-DTI-EXT-MIB", "ciscoDtiExtNotifsControlGroup"),
        ("CISCO-DTI-EXT-MIB", "ciscoDtiExtNotifsGroup"))
)
if mibBuilder.loadTexts:
    ciscoDtiExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DTI-EXT-MIB",
    **{"ciscoDtiExtMIB": ciscoDtiExtMIB,
       "ciscoDtiExtNotifs": ciscoDtiExtNotifs,
       "cdeServerStatusChange": cdeServerStatusChange,
       "cdeClientStatusChange": cdeClientStatusChange,
       "ciscoDtiExtObjects": ciscoDtiExtObjects,
       "cdeServerStatusChangeEnable": cdeServerStatusChangeEnable,
       "cdeClientStatusChangeEnable": cdeClientStatusChangeEnable,
       "ciscoDtiExtConform": ciscoDtiExtConform,
       "ciscoDtiExtCompliances": ciscoDtiExtCompliances,
       "ciscoDtiExtCompliance": ciscoDtiExtCompliance,
       "ciscoDtiExtGroups": ciscoDtiExtGroups,
       "ciscoDtiExtNotifsControlGroup": ciscoDtiExtNotifsControlGroup,
       "ciscoDtiExtNotifsGroup": ciscoDtiExtNotifsGroup}
)
