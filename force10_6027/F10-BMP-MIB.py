# SNMP MIB module (F10-BMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/force10_6027/F10-BMP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:18:14 2025
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

(f10Mgmt,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Mgmt")

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

f10BmpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 23)
)
if mibBuilder.loadTexts:
    f10BmpMib.setRevisions(
        ("2014-07-21 12:00",
         "2011-12-07 12:48")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F10Bmp_ObjectIdentity = ObjectIdentity
f10Bmp = _F10Bmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 23, 1)
)


class _BmpReloadType_Type(Integer32):
    """Custom type bmpReloadType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalReload", 1),
          ("bmpReload", 2))
    )


_BmpReloadType_Type.__name__ = "Integer32"
_BmpReloadType_Object = MibScalar
bmpReloadType = _BmpReloadType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 23, 1, 1),
    _BmpReloadType_Type()
)
bmpReloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmpReloadType.setStatus("current")


class _BmpAutoSave_Type(Integer32):
    """Custom type bmpAutoSave based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bmpActionEnable", 1),
          ("bmpActionDisable", 2))
    )


_BmpAutoSave_Type.__name__ = "Integer32"
_BmpAutoSave_Object = MibScalar
bmpAutoSave = _BmpAutoSave_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 23, 1, 2),
    _BmpAutoSave_Type()
)
bmpAutoSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmpAutoSave.setStatus("current")


class _BmpConfigDownload_Type(Integer32):
    """Custom type bmpConfigDownload based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bmpActionEnable", 1),
          ("bmpActionDisable", 2))
    )


_BmpConfigDownload_Type.__name__ = "Integer32"
_BmpConfigDownload_Object = MibScalar
bmpConfigDownload = _BmpConfigDownload_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 23, 1, 3),
    _BmpConfigDownload_Type()
)
bmpConfigDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmpConfigDownload.setStatus("current")


class _BmpDhcpTimeout_Type(Integer32):
    """Custom type bmpDhcpTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_BmpDhcpTimeout_Type.__name__ = "Integer32"
_BmpDhcpTimeout_Object = MibScalar
bmpDhcpTimeout = _BmpDhcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 23, 1, 4),
    _BmpDhcpTimeout_Type()
)
bmpDhcpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmpDhcpTimeout.setStatus("current")


class _BmpRetryCount_Type(Integer32):
    """Custom type bmpRetryCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_BmpRetryCount_Type.__name__ = "Integer32"
_BmpRetryCount_Object = MibScalar
bmpRetryCount = _BmpRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 23, 1, 5),
    _BmpRetryCount_Type()
)
bmpRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmpRetryCount.setStatus("current")


class _BmpUserDefinedString_Type(OctetString):
    """Custom type bmpUserDefinedString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BmpUserDefinedString_Type.__name__ = "OctetString"
_BmpUserDefinedString_Object = MibScalar
bmpUserDefinedString = _BmpUserDefinedString_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 23, 1, 6),
    _BmpUserDefinedString_Type()
)
bmpUserDefinedString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmpUserDefinedString.setStatus("current")


class _BmpRelay_Type(Integer32):
    """Custom type bmpRelay based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bmpActionEnable", 1),
          ("bmpActionDisable", 2))
    )


_BmpRelay_Type.__name__ = "Integer32"
_BmpRelay_Object = MibScalar
bmpRelay = _BmpRelay_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 23, 1, 7),
    _BmpRelay_Type()
)
bmpRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmpRelay.setStatus("current")


class _BmpRelayRemoteId_Type(OctetString):
    """Custom type bmpRelayRemoteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BmpRelayRemoteId_Type.__name__ = "OctetString"
_BmpRelayRemoteId_Object = MibScalar
bmpRelayRemoteId = _BmpRelayRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 23, 1, 8),
    _BmpRelayRemoteId_Type()
)
bmpRelayRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmpRelayRemoteId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F10-BMP-MIB",
    **{"f10BmpMib": f10BmpMib,
       "f10Bmp": f10Bmp,
       "bmpReloadType": bmpReloadType,
       "bmpAutoSave": bmpAutoSave,
       "bmpConfigDownload": bmpConfigDownload,
       "bmpDhcpTimeout": bmpDhcpTimeout,
       "bmpRetryCount": bmpRetryCount,
       "bmpUserDefinedString": bmpUserDefinedString,
       "bmpRelay": bmpRelay,
       "bmpRelayRemoteId": bmpRelayRemoteId}
)
