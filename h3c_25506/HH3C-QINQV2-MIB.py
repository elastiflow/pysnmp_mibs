# SNMP MIB module (HH3C-QINQV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/h3c_25506/HH3C-QINQV2-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:42:37 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cQinQv2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 137)
)
if mibBuilder.loadTexts:
    hh3cQinQv2.setRevisions(
        ("2013-03-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cQinQv2MibObject_ObjectIdentity = ObjectIdentity
hh3cQinQv2MibObject = _Hh3cQinQv2MibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 137, 1)
)
_Hh3cQinQv2ScalarObjects_ObjectIdentity = ObjectIdentity
hh3cQinQv2ScalarObjects = _Hh3cQinQv2ScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 137, 1, 1)
)


class _Hh3cQinQv2ServiceTPID_Type(Integer32):
    """Custom type hh3cQinQv2ServiceTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQinQv2ServiceTPID_Type.__name__ = "Integer32"
_Hh3cQinQv2ServiceTPID_Object = MibScalar
hh3cQinQv2ServiceTPID = _Hh3cQinQv2ServiceTPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 137, 1, 1, 1),
    _Hh3cQinQv2ServiceTPID_Type()
)
hh3cQinQv2ServiceTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQinQv2ServiceTPID.setStatus("current")


class _Hh3cQinQv2CustomerTPID_Type(Integer32):
    """Custom type hh3cQinQv2CustomerTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQinQv2CustomerTPID_Type.__name__ = "Integer32"
_Hh3cQinQv2CustomerTPID_Object = MibScalar
hh3cQinQv2CustomerTPID = _Hh3cQinQv2CustomerTPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 137, 1, 1, 2),
    _Hh3cQinQv2CustomerTPID_Type()
)
hh3cQinQv2CustomerTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQinQv2CustomerTPID.setStatus("current")
_Hh3cQinQv2IfCfgTable_Object = MibTable
hh3cQinQv2IfCfgTable = _Hh3cQinQv2IfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 137, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cQinQv2IfCfgTable.setStatus("current")
_Hh3cQinQv2IfCfgEntry_Object = MibTableRow
hh3cQinQv2IfCfgEntry = _Hh3cQinQv2IfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 137, 1, 2, 1)
)
hh3cQinQv2IfCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cQinQv2IfCfgEntry.setStatus("current")


class _Hh3cQinQv2IfState_Type(TruthValue):
    """Custom type hh3cQinQv2IfState based on TruthValue"""
    defaultValue = 2


_Hh3cQinQv2IfState_Type.__name__ = "TruthValue"
_Hh3cQinQv2IfState_Object = MibTableColumn
hh3cQinQv2IfState = _Hh3cQinQv2IfState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 137, 1, 2, 1, 1),
    _Hh3cQinQv2IfState_Type()
)
hh3cQinQv2IfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQinQv2IfState.setStatus("current")


class _Hh3cQinQv2IfServiceTPID_Type(Integer32):
    """Custom type hh3cQinQv2IfServiceTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQinQv2IfServiceTPID_Type.__name__ = "Integer32"
_Hh3cQinQv2IfServiceTPID_Object = MibTableColumn
hh3cQinQv2IfServiceTPID = _Hh3cQinQv2IfServiceTPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 137, 1, 2, 1, 2),
    _Hh3cQinQv2IfServiceTPID_Type()
)
hh3cQinQv2IfServiceTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQinQv2IfServiceTPID.setStatus("current")


class _Hh3cQinQv2IfCustomerTPID_Type(Integer32):
    """Custom type hh3cQinQv2IfCustomerTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cQinQv2IfCustomerTPID_Type.__name__ = "Integer32"
_Hh3cQinQv2IfCustomerTPID_Object = MibTableColumn
hh3cQinQv2IfCustomerTPID = _Hh3cQinQv2IfCustomerTPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 137, 1, 2, 1, 3),
    _Hh3cQinQv2IfCustomerTPID_Type()
)
hh3cQinQv2IfCustomerTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQinQv2IfCustomerTPID.setStatus("current")


class _Hh3cQinQv2IfTransVlanList_Type(OctetString):
    """Custom type hh3cQinQv2IfTransVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixedLength = 512


_Hh3cQinQv2IfTransVlanList_Type.__name__ = "OctetString"
_Hh3cQinQv2IfTransVlanList_Object = MibTableColumn
hh3cQinQv2IfTransVlanList = _Hh3cQinQv2IfTransVlanList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 137, 1, 2, 1, 4),
    _Hh3cQinQv2IfTransVlanList_Type()
)
hh3cQinQv2IfTransVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQinQv2IfTransVlanList.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-QINQV2-MIB",
    **{"hh3cQinQv2": hh3cQinQv2,
       "hh3cQinQv2MibObject": hh3cQinQv2MibObject,
       "hh3cQinQv2ScalarObjects": hh3cQinQv2ScalarObjects,
       "hh3cQinQv2ServiceTPID": hh3cQinQv2ServiceTPID,
       "hh3cQinQv2CustomerTPID": hh3cQinQv2CustomerTPID,
       "hh3cQinQv2IfCfgTable": hh3cQinQv2IfCfgTable,
       "hh3cQinQv2IfCfgEntry": hh3cQinQv2IfCfgEntry,
       "hh3cQinQv2IfState": hh3cQinQv2IfState,
       "hh3cQinQv2IfServiceTPID": hh3cQinQv2IfServiceTPID,
       "hh3cQinQv2IfCustomerTPID": hh3cQinQv2IfCustomerTPID,
       "hh3cQinQv2IfTransVlanList": hh3cQinQv2IfTransVlanList}
)
