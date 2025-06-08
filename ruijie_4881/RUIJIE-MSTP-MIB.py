# SNMP MIB module (RUIJIE-MSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-MSTP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:12 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex")

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

ruijieMstpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 167)
)
if mibBuilder.loadTexts:
    ruijieMstpMIB.setRevisions(
        ("2021-02-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieMstpMibObjects_ObjectIdentity = ObjectIdentity
ruijieMstpMibObjects = _RuijieMstpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 167, 1)
)
_RuijieMstpPortTable_Object = MibTable
ruijieMstpPortTable = _RuijieMstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 167, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieMstpPortTable.setStatus("current")
_RuijieMstpPortEntry_Object = MibTableRow
ruijieMstpPortEntry = _RuijieMstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 167, 1, 1, 1)
)
ruijieMstpPortEntry.setIndexNames(
    (0, "RUIJIE-MSTP-MIB", "ruijieMstpPortIndex"),
    (0, "RUIJIE-MSTP-MIB", "ruijieMstpInstanceID"),
    (0, "RUIJIE-MSTP-MIB", "ruijieMstpPortName"),
)
if mibBuilder.loadTexts:
    ruijieMstpPortEntry.setStatus("current")
_RuijieMstpPortIndex_Type = IfIndex
_RuijieMstpPortIndex_Object = MibTableColumn
ruijieMstpPortIndex = _RuijieMstpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 167, 1, 1, 1, 1),
    _RuijieMstpPortIndex_Type()
)
ruijieMstpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieMstpPortIndex.setStatus("current")


class _RuijieMstpInstanceID_Type(Unsigned32):
    """Custom type ruijieMstpInstanceID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_RuijieMstpInstanceID_Type.__name__ = "Unsigned32"
_RuijieMstpInstanceID_Object = MibTableColumn
ruijieMstpInstanceID = _RuijieMstpInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 167, 1, 1, 1, 2),
    _RuijieMstpInstanceID_Type()
)
ruijieMstpInstanceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieMstpInstanceID.setStatus("current")
_RuijieMstpPortName_Type = DisplayString
_RuijieMstpPortName_Object = MibTableColumn
ruijieMstpPortName = _RuijieMstpPortName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 167, 1, 1, 1, 3),
    _RuijieMstpPortName_Type()
)
ruijieMstpPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieMstpPortName.setStatus("current")
_RuijieMstpTraps_ObjectIdentity = ObjectIdentity
ruijieMstpTraps = _RuijieMstpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 167, 2)
)

# Managed Objects groups


# Notification objects

ruijieMstpPortStateForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 167, 2, 1)
)
ruijieMstpPortStateForwarding.setObjects(
      *(("RUIJIE-MSTP-MIB", "ruijieMstpPortIndex"),
        ("RUIJIE-MSTP-MIB", "ruijieMstpPortName"),
        ("RUIJIE-MSTP-MIB", "ruijieMstpInstanceID"))
)
if mibBuilder.loadTexts:
    ruijieMstpPortStateForwarding.setStatus(
        "current"
    )

ruijieMstpPortStateDiscarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 167, 2, 2)
)
ruijieMstpPortStateDiscarding.setObjects(
      *(("RUIJIE-MSTP-MIB", "ruijieMstpPortIndex"),
        ("RUIJIE-MSTP-MIB", "ruijieMstpPortName"),
        ("RUIJIE-MSTP-MIB", "ruijieMstpInstanceID"))
)
if mibBuilder.loadTexts:
    ruijieMstpPortStateDiscarding.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-MSTP-MIB",
    **{"ruijieMstpMIB": ruijieMstpMIB,
       "ruijieMstpMibObjects": ruijieMstpMibObjects,
       "ruijieMstpPortTable": ruijieMstpPortTable,
       "ruijieMstpPortEntry": ruijieMstpPortEntry,
       "ruijieMstpPortIndex": ruijieMstpPortIndex,
       "ruijieMstpInstanceID": ruijieMstpInstanceID,
       "ruijieMstpPortName": ruijieMstpPortName,
       "ruijieMstpTraps": ruijieMstpTraps,
       "ruijieMstpPortStateForwarding": ruijieMstpPortStateForwarding,
       "ruijieMstpPortStateDiscarding": ruijieMstpPortStateDiscarding}
)
