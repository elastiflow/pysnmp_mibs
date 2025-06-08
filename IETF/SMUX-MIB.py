# SNMP MIB module (SMUX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/SMUX-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 15:00:24 2025
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

(MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn) = mibBuilder.importSymbols(
    "RFC1212",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Unix_ObjectIdentity = ObjectIdentity
unix = _Unix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4)
)
_Smux_ObjectIdentity = ObjectIdentity
smux = _Smux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4, 4)
)
_SmuxPeerTable_Object = MibTable
smuxPeerTable = _SmuxPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    smuxPeerTable.setStatus("mandatory")
_SmuxPeerEntry_Object = MibTableRow
smuxPeerEntry = _SmuxPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4, 4, 1, 1)
)
smuxPeerEntry.setIndexNames(
    (0, "SMUX-MIB", "smuxPindex"),
)
if mibBuilder.loadTexts:
    smuxPeerEntry.setStatus("mandatory")
_SmuxPindex_Type = Integer32
_SmuxPindex_Object = MibTableColumn
smuxPindex = _SmuxPindex_Object(
    (1, 3, 6, 1, 4, 1, 4, 4, 1, 1, 1),
    _SmuxPindex_Type()
)
smuxPindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smuxPindex.setStatus("mandatory")
_SmuxPidentity_Type = ObjectIdentifier
_SmuxPidentity_Object = MibTableColumn
smuxPidentity = _SmuxPidentity_Object(
    (1, 3, 6, 1, 4, 1, 4, 4, 1, 1, 2),
    _SmuxPidentity_Type()
)
smuxPidentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smuxPidentity.setStatus("mandatory")


class _SmuxPdescription_Type(DisplayString):
    """Custom type smuxPdescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SmuxPdescription_Type.__name__ = "DisplayString"
_SmuxPdescription_Object = MibTableColumn
smuxPdescription = _SmuxPdescription_Object(
    (1, 3, 6, 1, 4, 1, 4, 4, 1, 1, 3),
    _SmuxPdescription_Type()
)
smuxPdescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smuxPdescription.setStatus("mandatory")


class _SmuxPstatus_Type(Integer32):
    """Custom type smuxPstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2),
          ("connecting", 3))
    )


_SmuxPstatus_Type.__name__ = "Integer32"
_SmuxPstatus_Object = MibTableColumn
smuxPstatus = _SmuxPstatus_Object(
    (1, 3, 6, 1, 4, 1, 4, 4, 1, 1, 4),
    _SmuxPstatus_Type()
)
smuxPstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smuxPstatus.setStatus("mandatory")
_SmuxTreeTable_Object = MibTable
smuxTreeTable = _SmuxTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 4, 4, 2)
)
if mibBuilder.loadTexts:
    smuxTreeTable.setStatus("mandatory")
_SmuxTreeEntry_Object = MibTableRow
smuxTreeEntry = _SmuxTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4, 4, 2, 1)
)
smuxTreeEntry.setIndexNames(
    (0, "SMUX-MIB", "smuxTsubtree"),
    (0, "SMUX-MIB", "smuxTpriority"),
)
if mibBuilder.loadTexts:
    smuxTreeEntry.setStatus("mandatory")
_SmuxTsubtree_Type = ObjectIdentifier
_SmuxTsubtree_Object = MibTableColumn
smuxTsubtree = _SmuxTsubtree_Object(
    (1, 3, 6, 1, 4, 1, 4, 4, 2, 1, 1),
    _SmuxTsubtree_Type()
)
smuxTsubtree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smuxTsubtree.setStatus("mandatory")


class _SmuxTpriority_Type(Integer32):
    """Custom type smuxTpriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SmuxTpriority_Type.__name__ = "Integer32"
_SmuxTpriority_Object = MibTableColumn
smuxTpriority = _SmuxTpriority_Object(
    (1, 3, 6, 1, 4, 1, 4, 4, 2, 1, 2),
    _SmuxTpriority_Type()
)
smuxTpriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smuxTpriority.setStatus("mandatory")
_SmuxTindex_Type = Integer32
_SmuxTindex_Object = MibTableColumn
smuxTindex = _SmuxTindex_Object(
    (1, 3, 6, 1, 4, 1, 4, 4, 2, 1, 3),
    _SmuxTindex_Type()
)
smuxTindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smuxTindex.setStatus("mandatory")


class _SmuxTstatus_Type(Integer32):
    """Custom type smuxTstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_SmuxTstatus_Type.__name__ = "Integer32"
_SmuxTstatus_Object = MibTableColumn
smuxTstatus = _SmuxTstatus_Object(
    (1, 3, 6, 1, 4, 1, 4, 4, 2, 1, 4),
    _SmuxTstatus_Type()
)
smuxTstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smuxTstatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SMUX-MIB",
    **{"unix": unix,
       "smux": smux,
       "smuxPeerTable": smuxPeerTable,
       "smuxPeerEntry": smuxPeerEntry,
       "smuxPindex": smuxPindex,
       "smuxPidentity": smuxPidentity,
       "smuxPdescription": smuxPdescription,
       "smuxPstatus": smuxPstatus,
       "smuxTreeTable": smuxTreeTable,
       "smuxTreeEntry": smuxTreeEntry,
       "smuxTsubtree": smuxTsubtree,
       "smuxTpriority": smuxTpriority,
       "smuxTindex": smuxTindex,
       "smuxTstatus": smuxTstatus}
)
