# SNMP MIB module (ZYXEL-STP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-STP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:33:35 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(zyMstpInstanceId,) = mibBuilder.importSymbols(
    "ZYXEL-MSTP-MIB",
    "zyMstpInstanceId")


# MODULE-IDENTITY

zyxelStp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MstiOrCistInstanceIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )



# MIB Managed Objects in the order of their OIDs

_ZyxelStpSetup_ObjectIdentity = ObjectIdentity
zyxelStpSetup = _ZyxelStpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 1)
)


class _ZyStpMode_Type(Integer32):
    """Custom type zyStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 1),
          ("mrstp", 2),
          ("mstp", 3))
    )


_ZyStpMode_Type.__name__ = "Integer32"
_ZyStpMode_Object = MibScalar
zyStpMode = _ZyStpMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 1, 1),
    _ZyStpMode_Type()
)
zyStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStpMode.setStatus("current")
_ZyStpRstpState_Type = EnabledStatus
_ZyStpRstpState_Object = MibScalar
zyStpRstpState = _ZyStpRstpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 1, 2),
    _ZyStpRstpState_Type()
)
zyStpRstpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStpRstpState.setStatus("current")
_ZyxelStpRootGuardRstpTable_Object = MibTable
zyxelStpRootGuardRstpTable = _ZyxelStpRootGuardRstpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelStpRootGuardRstpTable.setStatus("current")
_ZyxelStpRootGuardRstpPortEntry_Object = MibTableRow
zyxelStpRootGuardRstpPortEntry = _ZyxelStpRootGuardRstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 1, 3, 1)
)
zyxelStpRootGuardRstpPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelStpRootGuardRstpPortEntry.setStatus("current")
_ZyStpRootGuardRstpState_Type = EnabledStatus
_ZyStpRootGuardRstpState_Object = MibTableColumn
zyStpRootGuardRstpState = _ZyStpRootGuardRstpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 1, 3, 1, 1),
    _ZyStpRootGuardRstpState_Type()
)
zyStpRootGuardRstpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStpRootGuardRstpState.setStatus("current")
_ZyxelStpRootGuardMrstpTable_Object = MibTable
zyxelStpRootGuardMrstpTable = _ZyxelStpRootGuardMrstpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 1, 4)
)
if mibBuilder.loadTexts:
    zyxelStpRootGuardMrstpTable.setStatus("current")
_ZyxelStpRootGuardMrstpPortEntry_Object = MibTableRow
zyxelStpRootGuardMrstpPortEntry = _ZyxelStpRootGuardMrstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 1, 4, 1)
)
zyxelStpRootGuardMrstpPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelStpRootGuardMrstpPortEntry.setStatus("current")
_ZyStpRootGuardMrstpState_Type = EnabledStatus
_ZyStpRootGuardMrstpState_Object = MibTableColumn
zyStpRootGuardMrstpState = _ZyStpRootGuardMrstpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 1, 4, 1, 1),
    _ZyStpRootGuardMrstpState_Type()
)
zyStpRootGuardMrstpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStpRootGuardMrstpState.setStatus("current")
_ZyxelStpRootGuardMstpTable_Object = MibTable
zyxelStpRootGuardMstpTable = _ZyxelStpRootGuardMstpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 1, 5)
)
if mibBuilder.loadTexts:
    zyxelStpRootGuardMstpTable.setStatus("current")
_ZyxelStpRootGuardMstpPortEntry_Object = MibTableRow
zyxelStpRootGuardMstpPortEntry = _ZyxelStpRootGuardMstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 1, 5, 1)
)
zyxelStpRootGuardMstpPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelStpRootGuardMstpPortEntry.setStatus("current")
_ZyStpRootGuardMstpState_Type = EnabledStatus
_ZyStpRootGuardMstpState_Object = MibTableColumn
zyStpRootGuardMstpState = _ZyStpRootGuardMstpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 1, 5, 1, 1),
    _ZyStpRootGuardMstpState_Type()
)
zyStpRootGuardMstpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStpRootGuardMstpState.setStatus("current")
_ZyxelStpStatus_ObjectIdentity = ObjectIdentity
zyxelStpStatus = _ZyxelStpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 2)
)
_ZyxelStpRootGuardTable_Object = MibTable
zyxelStpRootGuardTable = _ZyxelStpRootGuardTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelStpRootGuardTable.setStatus("current")
_ZyxelStpRootGuardEntry_Object = MibTableRow
zyxelStpRootGuardEntry = _ZyxelStpRootGuardEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 2, 1, 1)
)
zyxelStpRootGuardEntry.setIndexNames(
    (0, "ZYXEL-STP-MIB", "zyStpRootGuardInstance"),
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelStpRootGuardEntry.setStatus("current")
_ZyStpRootGuardInstance_Type = MstiOrCistInstanceIndex
_ZyStpRootGuardInstance_Object = MibTableColumn
zyStpRootGuardInstance = _ZyStpRootGuardInstance_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 2, 1, 1, 1),
    _ZyStpRootGuardInstance_Type()
)
zyStpRootGuardInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyStpRootGuardInstance.setStatus("current")


class _ZyStpRootGuardStatus_Type(Integer32):
    """Custom type zyStpRootGuardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 0),
          ("rootInconsistent", 1))
    )


_ZyStpRootGuardStatus_Type.__name__ = "Integer32"
_ZyStpRootGuardStatus_Object = MibTableColumn
zyStpRootGuardStatus = _ZyStpRootGuardStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 2, 1, 1, 2),
    _ZyStpRootGuardStatus_Type()
)
zyStpRootGuardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyStpRootGuardStatus.setStatus("current")
_ZyxelStpNotifications_ObjectIdentity = ObjectIdentity
zyxelStpNotifications = _ZyxelStpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 3)
)

# Managed Objects groups


# Notification objects

zyStpRootGuardDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 3, 1)
)
zyStpRootGuardDetect.setObjects(
      *(("ZYXEL-STP-MIB", "zyStpMode"),
        ("ZYXEL-MSTP-MIB", "zyMstpInstanceId"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    zyStpRootGuardDetect.setStatus(
        "current"
    )

zyStpRootGuardRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 79, 3, 2)
)
zyStpRootGuardRecovered.setObjects(
      *(("ZYXEL-STP-MIB", "zyStpMode"),
        ("ZYXEL-MSTP-MIB", "zyMstpInstanceId"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    zyStpRootGuardRecovered.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-STP-MIB",
    **{"MstiOrCistInstanceIndex": MstiOrCistInstanceIndex,
       "zyxelStp": zyxelStp,
       "zyxelStpSetup": zyxelStpSetup,
       "zyStpMode": zyStpMode,
       "zyStpRstpState": zyStpRstpState,
       "zyxelStpRootGuardRstpTable": zyxelStpRootGuardRstpTable,
       "zyxelStpRootGuardRstpPortEntry": zyxelStpRootGuardRstpPortEntry,
       "zyStpRootGuardRstpState": zyStpRootGuardRstpState,
       "zyxelStpRootGuardMrstpTable": zyxelStpRootGuardMrstpTable,
       "zyxelStpRootGuardMrstpPortEntry": zyxelStpRootGuardMrstpPortEntry,
       "zyStpRootGuardMrstpState": zyStpRootGuardMrstpState,
       "zyxelStpRootGuardMstpTable": zyxelStpRootGuardMstpTable,
       "zyxelStpRootGuardMstpPortEntry": zyxelStpRootGuardMstpPortEntry,
       "zyStpRootGuardMstpState": zyStpRootGuardMstpState,
       "zyxelStpStatus": zyxelStpStatus,
       "zyxelStpRootGuardTable": zyxelStpRootGuardTable,
       "zyxelStpRootGuardEntry": zyxelStpRootGuardEntry,
       "zyStpRootGuardInstance": zyStpRootGuardInstance,
       "zyStpRootGuardStatus": zyStpRootGuardStatus,
       "zyxelStpNotifications": zyxelStpNotifications,
       "zyStpRootGuardDetect": zyStpRootGuardDetect,
       "zyStpRootGuardRecovered": zyStpRootGuardRecovered}
)
