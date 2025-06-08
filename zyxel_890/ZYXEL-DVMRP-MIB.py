# SNMP MIB module (ZYXEL-DVMRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-DVMRP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:25:24 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")

(zyRouteDomainIpAddress,
 zyRouteDomainIpMaskBits) = mibBuilder.importSymbols(
    "ZYXEL-IP-FORWARD-MIB",
    "zyRouteDomainIpAddress",
    "zyRouteDomainIpMaskBits")


# MODULE-IDENTITY

zyxelDvmrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelDvmrpSetup_ObjectIdentity = ObjectIdentity
zyxelDvmrpSetup = _ZyxelDvmrpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1)
)
_ZyDvmrpState_Type = EnabledStatus
_ZyDvmrpState_Object = MibScalar
zyDvmrpState = _ZyDvmrpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 1),
    _ZyDvmrpState_Type()
)
zyDvmrpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDvmrpState.setStatus("current")
_ZyDvmrpThreshold_Type = Integer32
_ZyDvmrpThreshold_Object = MibScalar
zyDvmrpThreshold = _ZyDvmrpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 2),
    _ZyDvmrpThreshold_Type()
)
zyDvmrpThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDvmrpThreshold.setStatus("current")
_ZyxelDvmrpRouteDomainTable_Object = MibTable
zyxelDvmrpRouteDomainTable = _ZyxelDvmrpRouteDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelDvmrpRouteDomainTable.setStatus("current")
_ZyxelDvmrpRouteDomainEntry_Object = MibTableRow
zyxelDvmrpRouteDomainEntry = _ZyxelDvmrpRouteDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 3, 1)
)
zyxelDvmrpRouteDomainEntry.setIndexNames(
    (0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpAddress"),
    (0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpMaskBits"),
)
if mibBuilder.loadTexts:
    zyxelDvmrpRouteDomainEntry.setStatus("current")
_ZyDvmrpRouteDomainState_Type = EnabledStatus
_ZyDvmrpRouteDomainState_Object = MibTableColumn
zyDvmrpRouteDomainState = _ZyDvmrpRouteDomainState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 3, 1, 1),
    _ZyDvmrpRouteDomainState_Type()
)
zyDvmrpRouteDomainState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDvmrpRouteDomainState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-DVMRP-MIB",
    **{"zyxelDvmrp": zyxelDvmrp,
       "zyxelDvmrpSetup": zyxelDvmrpSetup,
       "zyDvmrpState": zyDvmrpState,
       "zyDvmrpThreshold": zyDvmrpThreshold,
       "zyxelDvmrpRouteDomainTable": zyxelDvmrpRouteDomainTable,
       "zyxelDvmrpRouteDomainEntry": zyxelDvmrpRouteDomainEntry,
       "zyDvmrpRouteDomainState": zyDvmrpRouteDomainState}
)
