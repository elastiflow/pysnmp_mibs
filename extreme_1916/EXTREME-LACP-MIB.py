# SNMP MIB module (EXTREME-LACP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-LACP-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:23:18 2025
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeLacp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LacpGroupId(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class LacpMemberPort(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_ExtremeLacpTable_Object = MibTable
extremeLacpTable = _ExtremeLacpTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 19, 1)
)
if mibBuilder.loadTexts:
    extremeLacpTable.setStatus("current")
_ExtremeLacpEntry_Object = MibTableRow
extremeLacpEntry = _ExtremeLacpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1)
)
extremeLacpEntry.setIndexNames(
    (0, "EXTREME-LACP-MIB", "extremeLacpGroup"),
    (0, "EXTREME-LACP-MIB", "extremeLacpMemberPort"),
)
if mibBuilder.loadTexts:
    extremeLacpEntry.setStatus("current")
_ExtremeLacpGroup_Type = LacpGroupId
_ExtremeLacpGroup_Object = MibTableColumn
extremeLacpGroup = _ExtremeLacpGroup_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1, 1),
    _ExtremeLacpGroup_Type()
)
extremeLacpGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLacpGroup.setStatus("current")
_ExtremeLacpMemberPort_Type = LacpMemberPort
_ExtremeLacpMemberPort_Object = MibTableColumn
extremeLacpMemberPort = _ExtremeLacpMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1, 2),
    _ExtremeLacpMemberPort_Type()
)
extremeLacpMemberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLacpMemberPort.setStatus("current")
_ExtremeLacpAggStatus_Type = TruthValue
_ExtremeLacpAggStatus_Object = MibTableColumn
extremeLacpAggStatus = _ExtremeLacpAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1, 3),
    _ExtremeLacpAggStatus_Type()
)
extremeLacpAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLacpAggStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-LACP-MIB",
    **{"LacpGroupId": LacpGroupId,
       "LacpMemberPort": LacpMemberPort,
       "extremeLacp": extremeLacp,
       "extremeLacpTable": extremeLacpTable,
       "extremeLacpEntry": extremeLacpEntry,
       "extremeLacpGroup": extremeLacpGroup,
       "extremeLacpMemberPort": extremeLacpMemberPort,
       "extremeLacpAggStatus": extremeLacpAggStatus}
)
