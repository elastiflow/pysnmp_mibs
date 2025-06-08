# SNMP MIB module (CISCO-DMN-DSG-LOCKLEVEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-DMN-DSG-LOCKLEVEL-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:04:33 2025
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDSGLockLevel = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22)
)
if mibBuilder.loadTexts:
    ciscoDSGLockLevel.setRevisions(
        ("2010-08-30 11:00",
         "2010-06-28 06:00",
         "2010-05-24 06:30",
         "2009-12-20 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _LockLevel_Type(Integer32):
    """Custom type lockLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_LockLevel_Type.__name__ = "Integer32"
_LockLevel_Object = MibScalar
lockLevel = _LockLevel_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 1),
    _LockLevel_Type()
)
lockLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lockLevel.setStatus("current")


class _LockLevelPWD_Type(DisplayString):
    """Custom type lockLevelPWD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_LockLevelPWD_Type.__name__ = "DisplayString"
_LockLevelPWD_Object = MibScalar
lockLevelPWD = _LockLevelPWD_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 2),
    _LockLevelPWD_Type()
)
lockLevelPWD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lockLevelPWD.setStatus("current")


class _LockLevelPWDCUR_Type(DisplayString):
    """Custom type lockLevelPWDCUR based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_LockLevelPWDCUR_Type.__name__ = "DisplayString"
_LockLevelPWDCUR_Object = MibScalar
lockLevelPWDCUR = _LockLevelPWDCUR_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 3),
    _LockLevelPWDCUR_Type()
)
lockLevelPWDCUR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lockLevelPWDCUR.setStatus("current")


class _LockLevelPWDNEW_Type(DisplayString):
    """Custom type lockLevelPWDNEW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_LockLevelPWDNEW_Type.__name__ = "DisplayString"
_LockLevelPWDNEW_Object = MibScalar
lockLevelPWDNEW = _LockLevelPWDNEW_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 4),
    _LockLevelPWDNEW_Type()
)
lockLevelPWDNEW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lockLevelPWDNEW.setStatus("current")


class _LockLevelPWDCONF_Type(DisplayString):
    """Custom type lockLevelPWDCONF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_LockLevelPWDCONF_Type.__name__ = "DisplayString"
_LockLevelPWDCONF_Object = MibScalar
lockLevelPWDCONF = _LockLevelPWDCONF_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 5),
    _LockLevelPWDCONF_Type()
)
lockLevelPWDCONF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lockLevelPWDCONF.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-LOCKLEVEL-MIB",
    **{"ciscoDSGLockLevel": ciscoDSGLockLevel,
       "lockLevel": lockLevel,
       "lockLevelPWD": lockLevelPWD,
       "lockLevelPWDCUR": lockLevelPWDCUR,
       "lockLevelPWDNEW": lockLevelPWDNEW,
       "lockLevelPWDCONF": lockLevelPWDCONF}
)
