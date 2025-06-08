# SNMP MIB module (EXTREME-HCLAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-HCLAG-MIB.mib
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

extremeHclag = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 38)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HclagGroupId(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class HclagMemberPort(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_ExtremeHclagTable_Object = MibTable
extremeHclagTable = _ExtremeHclagTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 38, 1)
)
if mibBuilder.loadTexts:
    extremeHclagTable.setStatus("current")
_ExtremeHclagEntry_Object = MibTableRow
extremeHclagEntry = _ExtremeHclagEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1)
)
extremeHclagEntry.setIndexNames(
    (0, "EXTREME-HCLAG-MIB", "extremeHclagGroup"),
    (0, "EXTREME-HCLAG-MIB", "extremeHclagMemberPort"),
)
if mibBuilder.loadTexts:
    extremeHclagEntry.setStatus("current")
_ExtremeHclagGroup_Type = HclagGroupId
_ExtremeHclagGroup_Object = MibTableColumn
extremeHclagGroup = _ExtremeHclagGroup_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 1),
    _ExtremeHclagGroup_Type()
)
extremeHclagGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeHclagGroup.setStatus("current")
_ExtremeHclagMemberPort_Type = HclagMemberPort
_ExtremeHclagMemberPort_Object = MibTableColumn
extremeHclagMemberPort = _ExtremeHclagMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 2),
    _ExtremeHclagMemberPort_Type()
)
extremeHclagMemberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeHclagMemberPort.setStatus("current")
_ExtremeHclagAdminState_Type = TruthValue
_ExtremeHclagAdminState_Object = MibTableColumn
extremeHclagAdminState = _ExtremeHclagAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 3),
    _ExtremeHclagAdminState_Type()
)
extremeHclagAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeHclagAdminState.setStatus("current")
_ExtremeHclagLinkState_Type = TruthValue
_ExtremeHclagLinkState_Object = MibTableColumn
extremeHclagLinkState = _ExtremeHclagLinkState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 4),
    _ExtremeHclagLinkState_Type()
)
extremeHclagLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeHclagLinkState.setStatus("current")
_ExtremeHclagStatus_Type = TruthValue
_ExtremeHclagStatus_Object = MibTableColumn
extremeHclagStatus = _ExtremeHclagStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 5),
    _ExtremeHclagStatus_Type()
)
extremeHclagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeHclagStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-HCLAG-MIB",
    **{"HclagGroupId": HclagGroupId,
       "HclagMemberPort": HclagMemberPort,
       "extremeHclag": extremeHclag,
       "extremeHclagTable": extremeHclagTable,
       "extremeHclagEntry": extremeHclagEntry,
       "extremeHclagGroup": extremeHclagGroup,
       "extremeHclagMemberPort": extremeHclagMemberPort,
       "extremeHclagAdminState": extremeHclagAdminState,
       "extremeHclagLinkState": extremeHclagLinkState,
       "extremeHclagStatus": extremeHclagStatus}
)
