# SNMP MIB module (DIGI-SOCKETID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-SOCKETID-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:54:31 2025
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

(digiSocketID,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiSocketID")

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


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class Switch(Integer32):
    """Custom type Switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SocketidTable_Object = MibTable
socketidTable = _SocketidTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 13, 11)
)
if mibBuilder.loadTexts:
    socketidTable.setStatus("mandatory")
_SocketidEntry_Object = MibTableRow
socketidEntry = _SocketidEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 13, 11, 1)
)
socketidEntry.setIndexNames(
    (0, "DIGI-SOCKETID-MIB", "socketidIndex"),
)
if mibBuilder.loadTexts:
    socketidEntry.setStatus("mandatory")
_SocketidIndex_Type = Integer32
_SocketidIndex_Object = MibTableColumn
socketidIndex = _SocketidIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 13, 11, 1, 11),
    _SocketidIndex_Type()
)
socketidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socketidIndex.setStatus("mandatory")
_SocketidState_Type = Switch
_SocketidState_Object = MibTableColumn
socketidState = _SocketidState_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 13, 11, 1, 12),
    _SocketidState_Type()
)
socketidState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketidState.setStatus("mandatory")
_SocketidString_Type = DisplayString
_SocketidString_Object = MibTableColumn
socketidString = _SocketidString_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 13, 11, 1, 13),
    _SocketidString_Type()
)
socketidString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketidString.setStatus("mandatory")


class _SocketidResetSettings_Type(Integer32):
    """Custom type socketidResetSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("factory", 2),
          ("nvram", 3))
    )


_SocketidResetSettings_Type.__name__ = "Integer32"
_SocketidResetSettings_Object = MibTableColumn
socketidResetSettings = _SocketidResetSettings_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 14, 13, 11, 1, 14),
    _SocketidResetSettings_Type()
)
socketidResetSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socketidResetSettings.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-SOCKETID-MIB",
    **{"DisplayString": DisplayString,
       "Switch": Switch,
       "socketidTable": socketidTable,
       "socketidEntry": socketidEntry,
       "socketidIndex": socketidIndex,
       "socketidState": socketidState,
       "socketidString": socketidString,
       "socketidResetSettings": socketidResetSettings}
)
