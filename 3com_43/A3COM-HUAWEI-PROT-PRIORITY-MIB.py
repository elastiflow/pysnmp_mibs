# SNMP MIB module (A3COM-HUAWEI-PROT-PRIORITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-PROT-PRIORITY-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:03:53 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

h3cProtocolPriority = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37)
)
if mibBuilder.loadTexts:
    h3cProtocolPriority.setRevisions(
        ("2005-01-17 16:33",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cProtocolPriorityObjects_ObjectIdentity = ObjectIdentity
h3cProtocolPriorityObjects = _H3cProtocolPriorityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1)
)
_H3cPPri_ObjectIdentity = ObjectIdentity
h3cPPri = _H3cPPri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1)
)
_H3cProtocolPriorityTable_Object = MibTable
h3cProtocolPriorityTable = _H3cProtocolPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cProtocolPriorityTable.setStatus("current")
_H3cProtocolPriorityEntry_Object = MibTableRow
h3cProtocolPriorityEntry = _H3cProtocolPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1, 1, 1)
)
h3cProtocolPriorityEntry.setIndexNames(
    (0, "A3COM-HUAWEI-PROT-PRIORITY-MIB", "h3cPPriProtocolType"),
)
if mibBuilder.loadTexts:
    h3cProtocolPriorityEntry.setStatus("current")


class _H3cPPriProtocolType_Type(Integer32):
    """Custom type h3cPPriProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ospf", 1),
          ("telnet", 2),
          ("snmp", 3),
          ("icmp", 4),
          ("bgp", 5),
          ("ldp", 6))
    )


_H3cPPriProtocolType_Type.__name__ = "Integer32"
_H3cPPriProtocolType_Object = MibTableColumn
h3cPPriProtocolType = _H3cPPriProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1, 1, 1, 1),
    _H3cPPriProtocolType_Type()
)
h3cPPriProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPPriProtocolType.setStatus("current")


class _H3cPPriPriorityType_Type(Integer32):
    """Custom type h3cPPriPriorityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipPrecedence", 1),
          ("dscp", 2))
    )


_H3cPPriPriorityType_Type.__name__ = "Integer32"
_H3cPPriPriorityType_Object = MibTableColumn
h3cPPriPriorityType = _H3cPPriPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1, 1, 1, 2),
    _H3cPPriPriorityType_Type()
)
h3cPPriPriorityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPPriPriorityType.setStatus("current")


class _H3cPPriPriorityVlaue_Type(Integer32):
    """Custom type h3cPPriPriorityVlaue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_H3cPPriPriorityVlaue_Type.__name__ = "Integer32"
_H3cPPriPriorityVlaue_Object = MibTableColumn
h3cPPriPriorityVlaue = _H3cPPriPriorityVlaue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1, 1, 1, 3),
    _H3cPPriPriorityVlaue_Type()
)
h3cPPriPriorityVlaue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPPriPriorityVlaue.setStatus("current")
_H3cPPriRowStatus_Type = RowStatus
_H3cPPriRowStatus_Object = MibTableColumn
h3cPPriRowStatus = _H3cPPriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1, 1, 1, 4),
    _H3cPPriRowStatus_Type()
)
h3cPPriRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPPriRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-PROT-PRIORITY-MIB",
    **{"h3cProtocolPriority": h3cProtocolPriority,
       "h3cProtocolPriorityObjects": h3cProtocolPriorityObjects,
       "h3cPPri": h3cPPri,
       "h3cProtocolPriorityTable": h3cProtocolPriorityTable,
       "h3cProtocolPriorityEntry": h3cProtocolPriorityEntry,
       "h3cPPriProtocolType": h3cPPriProtocolType,
       "h3cPPriPriorityType": h3cPPriPriorityType,
       "h3cPPriPriorityVlaue": h3cPPriPriorityVlaue,
       "h3cPPriRowStatus": h3cPPriRowStatus}
)
