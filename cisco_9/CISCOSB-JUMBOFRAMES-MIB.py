# SNMP MIB module (CISCOSB-JUMBOFRAMES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCOSB-JUMBOFRAMES-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:12:46 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

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

rlJumboFrames = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 91)
)
if mibBuilder.loadTexts:
    rlJumboFrames.setRevisions(
        ("2007-01-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RlJumboFramesCurrentStatus_Type(Integer32):
    """Custom type rlJumboFramesCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RlJumboFramesCurrentStatus_Type.__name__ = "Integer32"
_RlJumboFramesCurrentStatus_Object = MibScalar
rlJumboFramesCurrentStatus = _RlJumboFramesCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 91, 1),
    _RlJumboFramesCurrentStatus_Type()
)
rlJumboFramesCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlJumboFramesCurrentStatus.setStatus("current")


class _RlJumboFramesStatusAfterReset_Type(Integer32):
    """Custom type rlJumboFramesStatusAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RlJumboFramesStatusAfterReset_Type.__name__ = "Integer32"
_RlJumboFramesStatusAfterReset_Object = MibScalar
rlJumboFramesStatusAfterReset = _RlJumboFramesStatusAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 91, 2),
    _RlJumboFramesStatusAfterReset_Type()
)
rlJumboFramesStatusAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlJumboFramesStatusAfterReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-JUMBOFRAMES-MIB",
    **{"rlJumboFrames": rlJumboFrames,
       "rlJumboFramesCurrentStatus": rlJumboFramesCurrentStatus,
       "rlJumboFramesStatusAfterReset": rlJumboFramesStatusAfterReset}
)
